from enum import Enum

from pydantic import BaseModel


class SortOption(BaseModel):
    id_: str
    selected: bool = False


class SortOptions(BaseModel):
    options: list[SortOption]

    @classmethod
    def from_values(cls, enum: Enum, selected: str = None):
        values = []
        for e in enum:
            values.append(SortOption(id_=e.value, selected=e.value == selected))
        return cls(options=values)


class PagingListResponse(BaseModel):
    items: list
    offset: int
    size: int
    total: int
    sort_options: SortOptions | None = None
    keyword: str | None = None

    @property
    def has_next(self) -> bool:
        return len(self.items) == self.size and (self.offset + self.size) < self.total

    @property
    def has_previous(self) -> bool:
        return self.offset > 0 and self.total > 1


def values_excluding_key(d: dict, k: str) -> list:
    return [d[k] for k in d.keys() - [k]]
