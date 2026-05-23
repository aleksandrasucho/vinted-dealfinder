from dataclasses import dataclass


@dataclass
class SearchRule:
    keyword: str
    max_price: float