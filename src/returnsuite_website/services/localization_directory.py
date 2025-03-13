from importlib.resources import files

from pydantic import BaseModel


class Language(BaseModel):
    name: str
    slug: str
    bundle: str
    currency_code: str
    currency_locale: str
    area_unit: str


class Country(BaseModel):
    code: str
    name: str
    languages: list[Language]

    def get_flag(self) -> str:
        file = files(
            "returnsuite_website") / "resources" / "localizations" / "flags" / f"{self.code}.svg"
        svg = file.read_text()
        clipped_svg = "".join(svg.partition('viewBox="0 0 640 480">\n')[2:]).replace(
            "</svg>\n", "").strip()
        return clipped_svg


class Countries(BaseModel):
    countries: list[Country]


def load2() -> list[Country]:
    file = files("returnsuite_website") / "resources" / "localizations" / "languages.json"
    text = file.read_text()
    countries = Countries.model_validate_json(text).countries
    print(countries)
    return countries
