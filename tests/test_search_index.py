# How to generate search data.
# 1) Convert the markdown document with extensions enabled.
# 2) Extract the table of contents tokens
# 3) Produce sections from the HTML
# 4) Feed these into the search
from html import escape
from html.parser import HTMLParser
from importlib.resources import files

import markdown

from returnsuite_website.services.search import SearchIndex, Page


def test_meh():
    file = files("returnsuite_website") / "content" / "en" / "docs" / "concepts" / "math" / "perpetuities.md"

    page = Page(file)

    #md = markdown.Markdown(extensions=['meta', 'toc'])
    #md.convert(file.read_text())
#
    #print()
    #print(md.toc_tokens)

    #search_plugin = SearchPlugin()

    #search_plugin.

    search_index = SearchIndex()
    search_index.add_entry_from_context(page)

    for entry in search_index.entries:
        print(entry)

    #nav_file = files("returnsuite_website") / "content" / "en" / "nav.yml"
    #pages = PageContent.load_pages(nav_file)

