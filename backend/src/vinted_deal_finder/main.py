from vinted_deal_finder.config import load_searches


def main() -> None:
    searches = load_searches("backend/config/searches.json")

    print("Vinted Deal Finder backend is running.")
    print(f"Loaded {len(searches)} searches:")

    for search in searches:
        print(f"- {search.keyword}, max price: {search.max_price}")


if __name__ == "__main__":
    main()