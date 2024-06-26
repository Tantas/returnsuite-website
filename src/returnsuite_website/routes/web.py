from fastapi import APIRouter

from returnsuite_website.routes import blog, contact, landing, styles, system

router = APIRouter(include_in_schema=False)
router.include_router(blog.router)
router.include_router(contact.router)
router.include_router(landing.router)
router.include_router(styles.router)
router.include_router(system.router)
