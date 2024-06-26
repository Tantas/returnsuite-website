from starlette.responses import RedirectResponse


async def custom_404_handler(_, __):
    return RedirectResponse("/", status_code=301)
