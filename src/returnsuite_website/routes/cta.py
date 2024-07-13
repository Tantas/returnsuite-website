from datetime import UTC, datetime
from typing import Annotated

from fastapi import APIRouter, Body
from pydantic import BaseModel, ConfigDict, EmailStr
from sqlalchemy import func
from starlette.requests import Request
from starlette.responses import JSONResponse

from returnsuite_website.services.database import (
    DBSession,
    DocumentationReview,
    NewsletterSubscription,
)

router = APIRouter()


class HelpfulForm(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    page_name: str
    helpful: bool


@router.post("/docs/was-this-page-helpful")
async def post_was_this_page_helpful(
    request: Request,
    db: DBSession,
    form: Annotated[HelpfulForm, Body()],
) -> JSONResponse:
    review = DocumentationReview(
        page_name=form.page_name,
        helpful=form.helpful,
        locale=request.headers.get("Accept-Language"),
        created=datetime.now(UTC),
        ip_address=request.client.host,
        user_agent=request.headers.get("User-Agent"),
    )
    db.add(review)
    db.commit()
    return JSONResponse({"status": "success"})


class NewsLetterSignup(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    email: EmailStr
    timezone: str | None


@router.post("/docs/newsletter-signup")
async def post_newsletter_signup(
    request: Request,
    db: DBSession,
    form: Annotated[NewsLetterSignup, Body()],
) -> JSONResponse:
    existing_subscription = (
        db.query(NewsletterSubscription)
        .where(func.lower(NewsletterSubscription.email) == func.lower(form.email))
        .one_or_none()
    )
    if not existing_subscription:
        subscription = NewsletterSubscription(
            email=form.email.lower(),
            locale=request.headers.get("Accept-Language"),
            timezone=form.timezone,
            created=datetime.now(UTC),
            ip_address=request.client.host,
            user_agent=request.headers.get("User-Agent"),
        )
        db.add(subscription)
        db.commit()
    return JSONResponse({"status": "success"})
