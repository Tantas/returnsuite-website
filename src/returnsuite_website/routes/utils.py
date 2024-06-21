import secrets
import string

from fastapi import Request


def generate_token(length: int) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def get_locale(request: Request) -> str | None:
    return request.headers.get("Accept-Language")
