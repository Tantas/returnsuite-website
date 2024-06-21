import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Sequence

from dns.resolver import NXDOMAIN, NoResolverConfiguration, Resolver
from loguru import logger

from returnsuite_website.core.config import get_app_settings

_ssl_context = ssl.create_default_context()


def able_to_deliver(email: str) -> bool:
    """
    Verifies that an email domain has an MX record.
    """
    host = email if "@" not in email else email.split("@")[-1]
    try:
        return len(Resolver().resolve(host, "MX")) > 0
    except NXDOMAIN:
        return False
    except NoResolverConfiguration:
        logger.warning(
            "Unable to validate email domain MX record. No resolvers. "
            "Does the server have internet access?"
        )
        return True


class EmailUndeliverableException(Exception):
    pass


def send_email(
    to_address: str | Sequence[str],
    callback_token: str,
    subject: str,
    text_body: str,
    html_body: str = None,
    from_address: str = None,
):
    app_settings = get_app_settings()
    if not app_settings.smtp_enabled:
        return

    # Make the addresses a list if they are not already.
    if isinstance(to_address, str):
        to_address = [to_address]

    # Create the email body. Places optional html after the plain text as the
    # preferred content if provided.
    for an_address in to_address:
        if not from_address:
            from_address = app_settings.smtp_from
        root = MIMEMultipart("mixed")
        if app_settings.smtp_aws_arn is not None:
            # https://docs.aws.amazon.com/ses/latest/APIReference/API_SendRawEmail.html
            root["X-SES-FROM-ARN"] = app_settings.smtp_aws_arn
        root["callback_token"] = callback_token
        root["Subject"] = subject
        root["From"] = from_address
        root["To"] = an_address

        message = MIMEMultipart("alternative")
        message.attach(MIMEText(text_body, "plain"))
        if html_body is not None:
            message.attach(MIMEText(html_body, "html"))
        root.attach(message)
        body = root.as_string()

        # Must separate manually for SSL certificate to validate.
        host, port = app_settings.smtp_host.split(":")

        # Send the email via the SMTP configuration.
        try:
            if app_settings.smtp_use_ssl:
                with smtplib.SMTP_SSL(
                    host=host, port=port, context=_ssl_context
                ) as server:
                    if (
                        app_settings.smtp_user is not None
                        and app_settings.smtp_password is not None
                    ):
                        server.login(
                            app_settings.smtp_user,
                            app_settings.smtp_password.get_secret_value(),
                        )
                    server.sendmail(
                        from_addr=from_address, to_addrs=an_address, msg=body
                    )
            else:
                with smtplib.SMTP(host=host, port=port) as server:
                    if (
                        app_settings.smtp_user is not None
                        and app_settings.smtp_password is not None
                    ):
                        server.login(
                            app_settings.smtp_user,
                            app_settings.smtp_password.get_secret_value(),
                        )
                    server.sendmail(
                        from_addr=from_address, to_addrs=an_address, msg=body
                    )
        except smtplib.SMTPDataError as error:
            raise EmailUndeliverableException(str(error))
