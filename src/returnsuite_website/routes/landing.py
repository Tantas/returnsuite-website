from datetime import UTC, datetime
from typing import Annotated

from fastapi import APIRouter, Depends, Form, Header, Request
from fastapi.responses import HTMLResponse
from loguru import logger
from starlette.responses import RedirectResponse

from returnsuite_website.core.config import get_app_settings
from returnsuite_website.core.html import templates
from returnsuite_website.routes.utils import generate_token, get_locale
from returnsuite_website.services.database import (
    DBSession,
    Waitlist,
    WaitlistStatus,
    is_ip_address_spam_waitlist,
)
from returnsuite_website.services.email import send_email
from returnsuite_website.services.spam import detected_injection, detected_spam

router = APIRouter(default_response_class=HTMLResponse)


@router.get("/brave")
@router.get("/")  # Must be the last entry to be used with 'for_url'.
async def get_index(request: Request, success: bool | None = None):
    logger.warning(f"User agent is {request.headers.get('User-Agent')}")
    return templates.TemplateResponse(
        request=request,
        name="index3.html.jinja2",
        context={"success": success},
    )


@router.get("/landing-new")
async def get_index_new(request: Request, success: bool | None = None):
    logger.warning(f"User agent is {request.headers.get('User-Agent')}")
    return templates.TemplateResponse(
        request=request,
        name="index3.html.jinja2",
        context={"success": success},
    )


@router.get("/view-demo")
async def get_view_demo(request: Request):
    if get_app_settings().hide_demo:
        return RedirectResponse("/")
    return templates.TemplateResponse(request=request, name="demo.html.jinja2")


@router.get("/about")
async def get_about(request: Request):
    return templates.TemplateResponse(request=request, name="about.html.jinja2")


class JoinWaitlistForm:
    def __init__(
        self,
        timezone: str | None = Form(None),
        name: str = Form(...),
        email: str = Form(...),
        organization: str = Form(...),
        usage: str = Form(...),
        linkedin_url: str | None = Form(None),
        twitter_url: str | None = Form(None),
        other_url: str | None = Form(None),
        message: str | None = Form(None),
    ):
        self.timezone = timezone
        self.name = name.strip()
        self.email = email.strip()
        self.organization = organization.strip()
        self.usage = usage.strip()
        self.linkedin_url = linkedin_url.strip() if linkedin_url else None
        self.twitter_url = twitter_url.strip() if twitter_url else None
        self.other_url = other_url.strip() if other_url else None
        self.message = message.strip() if message else None

    def _likely_spam(self) -> bool:
        if "company.com" in self.email.lower():
            return True
        if "company name" in self.organization.lower():
            return True
        if "gmxxail.com" in self.email.lower():
            return True
        if detected_spam(self.message):
            return True
        if self.linkedin_url is not None and "no-site.com" in self.linkedin_url:
            return True
        if self.twitter_url is not None and "no-site.com" in self.twitter_url:
            return True
        if self.other_url is not None and "no-site.com" in self.other_url:
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
    ) -> Waitlist:
        status = WaitlistStatus.spam if self._likely_spam() else WaitlistStatus.waiting
        return Waitlist(
            status=status,
            locale=locale,
            timezone=self.timezone,
            name=self.name,
            email=self.email,
            organization=self.organization,
            usage=self.usage,
            created=now,
            linkedin_url=self.linkedin_url,
            twitter_url=self.twitter_url,
            other_url=self.other_url,
            message=self.message,
            ip_address=ip_address,
            user_agent=user_agent,
        )


@router.post("/waitlist")
async def post_waitlist(
    request: Request,
    db: DBSession,
    locale: Annotated[str, Depends(get_locale)],
    form: Annotated[JoinWaitlistForm, Depends()],
    user_agent: str | None = Header(None),
):
    ip_address = request.client.host
    join_request = form.to_request(datetime.now(UTC), locale, ip_address, user_agent)
    if is_ip_address_spam_waitlist(db, ip_address):
        join_request.status = WaitlistStatus.spam
    db.add(join_request)
    db.commit()

    if join_request.status is not WaitlistStatus.spam:
        send_email(
            to_address=get_app_settings().landing_contact_email,
            callback_token=generate_token(16),
            subject="Request to join the ReturnSuite waitlist",
            text_body=(
                f"Name: {join_request.name}\n"
                f"Organization: {join_request.organization if not None else '-'}\n"
                f"Usage: {join_request.usage}\n"
                f"Email: {join_request.email}\n"
                f"LinkedIn Profile: {join_request.linkedin_url}\n"
                f"Twitter Profile: {join_request.twitter_url}\n"
                f"Other Profile: {join_request.other_url}\n"
                f"Locale: {join_request.locale if not None else '-'}\n"
                f"Timezone: {join_request.timezone if not None else '-'}\n"
                f"Time and Date: {join_request.created}\n"
                f"IP Address: {ip_address}\n"
                f"User Agent: {user_agent}\n"
                f"Message: {join_request.message}\n"
            ),
        )
    else:
        logger.info(
            f"Received waitlist request likely spam: {form.name} {form.organization} "
            f"{form.email} {form.message}"
        )

    return RedirectResponse(
        f"{request.url_for('get_index').include_query_params(success='true')}"
        f"#Request-Early-Access",
        status_code=302,
    )


@router.get("/privacy")
async def get_privacy_policy(request: Request):
    return templates.TemplateResponse(request=request, name="privacy.html.jinja2")


@router.get("/terms")
async def get_terms_and_conditions(request: Request):
    return templates.TemplateResponse(request=request, name="terms.html.jinja2")


@router.get("/landing-images")
async def get_landing_images(request: Request):
    """
    Private page used to create the landing page feature images with the
    existing styles. Raster images are taken from this page.
    """
    return templates.TemplateResponse(
        request=request, name="landing-images2.html.jinja2"
    )
