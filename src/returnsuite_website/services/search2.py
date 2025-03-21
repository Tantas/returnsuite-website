from lunr import lunr
from pydantic import BaseModel

from returnsuite_website.services.docs_service import find_page, Page


class SearchResult(BaseModel):
    route: str
    title: str
    description: str
    breadcrumbs: list[str]
    score: float


class SearchIndex:

    def __init__(self, root: Page):
        self.pages = root
        documents = []

        def recurse(page: Page):
            documents.append({
                "id": page.route,
                "title": page.nav_title,
                "body": page.content
            })
            for child in page.children or []:
                recurse(child)

        recurse(root)

        self.idx = lunr(ref="id", fields=["title", "body"], documents=documents)

    def search(self, query: str) -> list[SearchResult]:
        results = []
        for result in self.idx.search(query):
            page = find_page(self.pages, result["ref"])
            score = result["score"]
            results.append(SearchResult(
                route=page.route,
                title=page.title,
                description=page.description,
                breadcrumbs=[x.nav_group for x in page.breadcrumbs][1:],
                score=score,
            ))
        return results
