import json
from pathlib import Path


def load_searches(config_path: str) -> list[dict]:
    path = Path(config_path)

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)