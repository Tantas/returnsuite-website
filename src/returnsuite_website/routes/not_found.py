from starlette.responses import RedirectResponse


async def custom_404_handler(_, __):
    print("Sending from here")
    return RedirectResponse("/", status_code=301)
