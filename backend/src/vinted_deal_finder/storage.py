import json
from pathlib import Path


def load_seen_listing_ids(path: str) -> set[str]:
    file_path = Path(path)

    if not file_path.exists():
        return set()

    with file_path.open("r", encoding="utf-8") as file:
        return set(json.load(file))


def save_seen_listing_ids(path: str, listing_ids: set[str]) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(sorted(listing_ids), file, indent=2)