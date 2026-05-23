import json
from pathlib import Path

from vinted_deal_finder.models import SearchRule


def load_searches(config_path: str) -> list[SearchRule]:
    path = Path(config_path)

    with path.open("r", encoding="utf-8") as file:
        raw_searches = json.load(file)

    return [
        SearchRule(
            keyword=item["keyword"],
            max_price=item["max_price"],
        )
        for item in raw_searches
    ]