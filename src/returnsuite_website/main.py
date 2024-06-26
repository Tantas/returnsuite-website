from pathlib import Path

import uvicorn
from fastapi import FastAPI
from starlette.middleware.gzip import GZipMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

from returnsuite_website.core import config
from returnsuite_website.routes import web
from returnsuite_website.routes.not_found import custom_404_handler
from returnsuite_website.routes.system import CacheControlledStaticFiles
from returnsuite_website.services import database


def get_application() -> FastAPI:
    settings = config.get_app_settings()
    settings.configure_logging()

    application = FastAPI(**settings.fastapi_kwargs)

    resources = f"{Path(__file__).parent.resolve()}/resources"
    application.mount(
        "/css", CacheControlledStaticFiles(directory=f"{resources}/css"), name="css"
    )
    application.mount(
        "/js", CacheControlledStaticFiles(directory=f"{resources}/js"), name="js"
    )
    application.mount(
        "/img", CacheControlledStaticFiles(directory=f"{resources}/img"), name="img"
    )
    application.include_router(web.router)
    application.add_exception_handler(404, custom_404_handler)

    if settings.compress_web_responses:
        # noinspection PyTypeChecker
        application.add_middleware(GZipMiddleware, minimum_size=1000)

    if settings.proxy_header_trusted_hosts:
        # noinspection PyTypeChecker
        application.add_middleware(
            ProxyHeadersMiddleware,
            trusted_hosts=settings.proxy_header_trusted_hosts,
        )

    if settings.create_database:
        database.create_all()

    return application


app = get_application()


def development_server():
    uvicorn.run("returnsuite_website.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    development_server()
