from dataclasses import dataclass


@dataclass
class SearchRule:
    keyword: str
    max_price: float


@dataclass
class Listing:
    id: str
    title: str
    price: float
    url: str