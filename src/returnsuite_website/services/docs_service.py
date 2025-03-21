import json
from importlib.resources import files
from importlib.resources.abc import Traversable
from typing import Self

import markdown
import yaml


class Page:

    def __init__(self, root: Traversable, filename: str, route: str, previous: Self | None):
        self.filename = filename
        self.route = route
        file = root / filename
        self.markdown = file.read_text()
        md = markdown.Markdown(extensions=["extra", "meta", "toc"])
        self.content = md.convert(self.markdown)

        # noinspection PyUnresolvedReferences
        self.toc = md.toc_tokens

        # noinspection PyUnresolvedReferences
        self.meta = md.Meta

        self.title = self.meta["title"][0]
        self.description = self.meta["description"][0]
        self.nav_title = self.meta["nav-title"][0]
        self.nav_group = self.meta["nav-group"][0]

        self.previous = previous
        self.next: Page | None = None

        self.children: list[Page] = []
        self.breadcrumbs: list[Page] = []


class Menu:

    def __init__(self, page: Page):
        self.nav_title = page.nav_title
        self.nav_group = page.nav_group
        self.route = page.route
        self.children = [Menu(child) for child in page.children]


def find_page(page: Page, path: str) -> Page | None:
    if path in page.route:
        return page
    for child in page.children:
        result = find_page(child, path)
        if result is not None:
            return result
    return None


def load_pages(root: Traversable) -> Page:
    previous = None

    def recurse(item: str | dict[str, str] | list, path: str = "") -> Page:
        nonlocal previous
        if isinstance(item, str):
            page = Page(root, item, path, previous)
            if previous:
                previous.next = page
            previous = page
            return page
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
    page_tree = recurse(data["nav"])

    # Produce the breadcrumbs for each page entry.
    def recurse_breadcrumbs(page: Page, crumbs: list[Page]):
        page.breadcrumbs = crumbs

        child_crumbs = [x for x in crumbs]
        child_crumbs.append(page)
        for child in page.children or []:
            recurse_breadcrumbs(child, child_crumbs)

    recurse_breadcrumbs(page_tree, [])
    return page_tree


def mobile_menu(root: Page) -> str:
    menu = Menu(root)
    print(json.dumps(menu.children, default=vars))
    return json.dumps(menu.children, default=vars)
