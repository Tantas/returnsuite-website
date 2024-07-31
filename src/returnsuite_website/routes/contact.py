from datetime import UTC, datetime
from typing import Annotated

from fastapi import APIRouter, Depends, Form, Header, Request
from loguru import logger
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.status import HTTP_302_FOUND

from returnsuite_website.core.config import get_app_settings
from returnsuite_website.core.html import templates
from returnsuite_website.routes.utils import generate_token, get_locale
from returnsuite_website.services.database import (
    ContactRequest,
    ContactRequestStatus,
    DBSession,
)
from returnsuite_website.services.email import send_email
from returnsuite_website.services.spam import detected_injection, detected_spam

router = APIRouter(default_response_class=HTMLResponse)


class ContactForm:
    def __init__(
        self,
        timezone: str | None = Form(None),
        name: str = Form(...),
        organization: str = Form(None),
        email: str = Form(..., pattern="^(.+)@(.+)$"),
        subject: str = Form(...),
        message: str | None = Form(...),
    ):
        self.timezone = timezone
        self.name = name.strip()
        self.organization = organization.strip() if organization else None
        self.email = email.strip().lower()
        self.subject = subject.strip()
        self.message = message.strip()

    def _likely_spam(self) -> bool:
        if "company.com" in self.email.lower():
            return True
        if detected_spam(self.message):
            return True
        if self.timezone is None or self.timezone in ("1", "n/c"):
            return True
        elif detected_injection(self.timezone):
            return True
        return False

    def to_request(
        self,
        now: datetime,
        locale: str | None,
        ip_address: str | None,
        user_agent: str | None,
    ) -> ContactRequest:
        status = (
            ContactRequestStatus.spam
            if self._likely_spam()
            else ContactRequestStatus.valid
        )
        return ContactRequest(
            status=status,
            locale=locale,
            timezone=self.timezone,
            name=self.name,
            email=self.email,
            organization=self.organization,
            created=now,
            subject=self.subject,
            message=self.message,
            ip_address=ip_address,
            user_agent=user_agent,
        )


@router.get("/contact")
async def get_contact(
    request: Request, success: bool | None = None, subject: str | None = None
):
    return templates.TemplateResponse(
        request=request,
        name="contact.html.jinja2",
        context={"success": success, "subject": subject},
    )


@router.post("/contact")
async def post_contact(
    request: Request,
    db: DBSession,
    form: Annotated[ContactForm, Depends()],
    locale: Annotated[str | None, Depends(get_locale)],
    user_agent: str | None = Header(None),
):
    ip_address = request.client.host
    contact_request = form.to_request(datetime.now(UTC), locale, ip_address, user_agent)
    db.add(contact_request)
    db.commit()

    if contact_request.status is not ContactRequestStatus.spam:
        send_email(
            to_address=get_app_settings().landing_contact_email,
            callback_token=generate_token(16),
            subject=f"ReturnSuite contact request: {form.subject}",
            text_body=(
                f"Name: {form.name}\n"
                f"Organization: {form.organization if not None else '-'}\n"
                f"Email: {form.email}\n"
                f"Locale: {locale if not None else '-'}\n"
                f"Timezone: {form.timezone if not None else '-'}\n"
                f"Time and Date: {datetime.now(UTC)}\n"
                f"IP Address: {ip_address}\n"
                f"User Agent: {user_agent}\n"
                f"Subject: {form.subject}\n"
                f"Message: {form.message}\n"
            ),
        )
    else:
        logger.info(
            f"Received contact request likely spam: {form.name} {form.organization} "
            f"{form.email} {form.subject} {form.message}"
        )

    return RedirectResponse(
        f"{request.url_for('get_contact').include_query_params(success='true')}",
        status_code=HTTP_302_FOUND,
    )
