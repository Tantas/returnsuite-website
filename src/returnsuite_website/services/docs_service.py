from importlib.resources import files
from importlib.resources.abc import Traversable

import markdown
import yaml


class Page:

    def __init__(self, root: Traversable, filename: str, route: str):
        self.filename = filename
        self.route = route
        file = root / filename
        self.markdown = file.read_text()
        md = markdown.Markdown(extensions=[
            "extra",
            "meta",
            "toc",
        ])
        self.content = md.convert(self.markdown)

        # noinspection PyUnresolvedReferences
        self.toc = md.toc_tokens  # get_toc(md.toc_tokens)

        # noinspection PyUnresolvedReferences
        self.meta = md.Meta

        self.title = self.meta["title"][0]
        self.description = self.meta["description"][0]
        self.nav_title = self.meta["nav-title"][0]
        self.nav_group = self.meta["nav-group"][0]

        self.previous: Page | None = None
        self.next: Page | None = None

        self.children: list[Page] = []


def find_page(page: Page, path: str) -> Page | None:
    if path in page.route:
        return page
    for child in page.children:
        result = find_page(child, path)
        if result is not None:
            return result
    return None


def load_pages(root: Traversable) -> Page:

    def recurse(item: str | dict[str, str] | list, path: str = "") -> Page:
        if isinstance(item, str):
            return Page(root, item, path)
        elif isinstance(item, dict):
            for entry in item.items():
                return recurse(entry[1], f"{path}/{entry[0]}")
        elif isinstance(item, list):
            list_root = recurse(item[0], path)
            for child in item[1:]:
                list_root.children.append(recurse(child, path))
            return list_root
        raise Exception(f"Malformed page for {root} {item}.")

    nav_file = root / "nav.yml"
    data = yaml.safe_load(nav_file.read_bytes())
    return recurse(data["nav"])


english_root = files("returnsuite_website") / "content" / "en"
root_page = load_pages(english_root)

print(root_page)
