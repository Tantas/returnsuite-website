from datetime import date
from enum import Enum
from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Depends, Query, Request
from pydantic import BaseModel, TypeAdapter
from starlette.responses import HTMLResponse, RedirectResponse

from returnsuite_website.core.html import templates
from returnsuite_website.routes.paging import PagingListResponse, SortOptions

router = APIRouter(default_response_class=HTMLResponse)


class BlogAuthor(BaseModel):
    name: str
    organization_title: str
    url: str
    profile_image_url: str | None = None


class BlogImage(BaseModel):
    alt: str
    url: str


class BlogPost(BaseModel):
    author: BlogAuthor
    category: str
    published: date
    original_publish_url: str | None = None
    slug: str
    title: str
    teaser: str
    teaser_image: BlogImage | None = None
    content: str


class BlogPosts(BaseModel):
    articles: list[BlogPost]


def get_posts() -> list[BlogPost]:
    type_adapter = TypeAdapter(BlogPosts)
    with open(f"{Path(__file__).parent.resolve()}/posts.json") as file:
        return type_adapter.validate_json(file.read()).articles


class BlogSort(str, Enum):
    spotlight = "spotlight"
    chronological = "chronological"

    @staticmethod
    def sort_chronologically(post: BlogPost):
        return post.published


class BlogListForm:
    def __init__(
        self,
        offset: str | int | None = Query(0),
        size: str | int | None = Query(5),
        sort: BlogSort | None = Query(BlogSort.spotlight),
    ):
        self.offset = int(offset) if offset else 0
        self.size = min(int(size) if size else 5, 10)
        self.sort = sort if sort else BlogSort.spotlight


@router.get("/blog")
async def get_blog(form: Annotated[BlogListForm, Depends()], request: Request):
    posts = get_posts()
    total_posts = len(posts)
    if total_posts <= form.offset:
        return RedirectResponse(request.url_for("get_blog"))
    if form.sort == BlogSort.chronological:
        posts.sort(key=BlogSort.sort_chronologically, reverse=True)
    page_response = PagingListResponse(
        items=posts[form.offset : form.offset + form.size],  # noqa: E203
        offset=form.offset,
        size=form.size,
        total=total_posts,
        sort_options=SortOptions.from_values(BlogSort, form.sort),
    )

    return templates.TemplateResponse(
        request=request,
        name="blog/index.html.jinja2",
        context={"page_response": page_response},
    )


@router.get("/blog/{slug}")
async def get_blog_post(request: Request, slug: str):
    post = None
    for possibility in get_posts():
        if possibility.slug == slug:
            post = possibility
    if not post:
        return RedirectResponse(request.url_for("get_blog"))
    return templates.TemplateResponse(
        request=request, name=f"blog/{post.content}", context={"post": post}
    )
