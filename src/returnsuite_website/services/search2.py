from lunr import lunr

from returnsuite_website.services.docs_service import find_page, Page


class SearchResult:

    def __init__(self, page: Page, score: float):
        self.route = page.route
        self.title = page.title
        # route
        # h1
        self.description = page.description
        self.breadcrumbs = ["Valuation Concepts", "Valuation Approaches"],
        self.score = score

    def __str__(self):
        return f"{self.score} {self.route}: {self.title}"


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
            results.append(SearchResult(page, score))
        return results
