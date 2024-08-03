from datetime import UTC, datetime, timedelta
from enum import Enum
from typing import Annotated

from fastapi import Depends
from sqlalchemy import DateTime, StaticPool, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

from returnsuite_website.core.config import get_app_settings
from returnsuite_website.core.settings.base import AppEnvTypes


class Base(DeclarativeBase):
    pass


class ContactRequestStatus(str, Enum):
    valid = "valid"
    invalid = "invalid"
    spam = "spam"


class ContactRequest(Base):
    __tablename__ = "contact_request"
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[ContactRequestStatus]
    locale: Mapped[str | None] = mapped_column(String(32))
    timezone: Mapped[str | None] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(255), index=True)
    email: Mapped[str] = mapped_column(String(255), index=True)
    organization: Mapped[str | None] = mapped_column(String(255))
    subject: Mapped[str] = mapped_column(String(255))
    message: Mapped[str] = mapped_column(Text)
    created: Mapped[datetime] = mapped_column(DateTime)
    note: Mapped[str | None] = mapped_column(Text)
    ip_address: Mapped[str | None] = mapped_column(String(128))
    user_agent: Mapped[str | None] = mapped_column(Text)


def is_ip_address_spam_contact(
    db: Session, ip_address: str, now: datetime = datetime.now(UTC)
) -> bool:
    return (
        db.query(ContactRequest)
        .where(ContactRequest.ip_address == ip_address)
        .where(ContactRequest.created >= (now - timedelta(hours=1)))
        .count()
    ) > 1


class WaitlistStatus(str, Enum):
    waiting = "waiting"
    accepted = "accepted"
    rejected = "rejected"
    invalid = "invalid"
    spam = "spam"


class Waitlist(Base):
    __tablename__ = "contact_waitlist"
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[WaitlistStatus]
    locale: Mapped[str | None] = mapped_column(String(32))
    timezone: Mapped[str | None] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(255), index=True)
    email: Mapped[str] = mapped_column(String(255), index=True)
    organization: Mapped[str] = mapped_column(String(255))
    usage: Mapped[str] = mapped_column(String(255))
    created: Mapped[datetime] = mapped_column(DateTime)
    linkedin_url: Mapped[str | None] = mapped_column(String(255))
    twitter_url: Mapped[str | None] = mapped_column(String(255))
    other_url: Mapped[str | None] = mapped_column(String(255))
    message: Mapped[str | None] = mapped_column(Text)
    note: Mapped[str | None] = mapped_column(Text)
    ip_address: Mapped[str | None] = mapped_column(String(128))
    user_agent: Mapped[str | None] = mapped_column(Text)


def is_ip_address_spam_waitlist(
    db: Session, ip_address: str, now: datetime = datetime.now(UTC)
) -> bool:
    return (
        db.query(Waitlist)
        .where(Waitlist.ip_address == ip_address)
        .where(Waitlist.created >= (now - timedelta(hours=1)))
        .count()
    ) > 1


class NewsletterSubscription(Base):
    __tablename__ = "contact_newsletter_subscription"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    locale: Mapped[str | None] = mapped_column(String(32))
    timezone: Mapped[str | None] = mapped_column(String(255))
    created: Mapped[datetime] = mapped_column(DateTime)
    ip_address: Mapped[str | None] = mapped_column(String(128))
    user_agent: Mapped[str | None] = mapped_column(Text)


class DocumentationReview(Base):
    __tablename__ = "contact_document_review"
    id: Mapped[int] = mapped_column(primary_key=True)
    page_name: Mapped[str] = mapped_column(String(255))
    helpful: Mapped[bool]
    locale: Mapped[str | None] = mapped_column(String(32))
    created: Mapped[datetime] = mapped_column(DateTime)
    ip_address: Mapped[str | None] = mapped_column(String(128))
    user_agent: Mapped[str | None] = mapped_column(Text)


if get_app_settings().app_env == AppEnvTypes.test:
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        echo=False,
        poolclass=StaticPool,
    )
else:
    # When the system is left idle over the MySQL default timeout, the
    # connection will be invalidated. `pool_recycle` will invalidate the
    # connection every hour ensuring an error does not occur.
    # See https://docs.sqlalchemy.org/en/20/core/pooling.html#setting-pool-recycle
    url = get_app_settings().database_url.get_secret_value()
    engine = create_engine(url, pool_recycle=3600)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def drop_all():
    Base.metadata.drop_all(bind=engine)


def create_all():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


DBSession = Annotated[Session, Depends(get_db)]
