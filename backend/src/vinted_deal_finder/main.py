from vinted_deal_finder.config import load_searches
from vinted_deal_finder.fetcher import fetch_listings


def main() -> None:
    searches = load_searches("backend/config/searches.json")

    print("Vinted Deal Finder backend is running.")
    print(f"Loaded {len(searches)} searches:")

    for search in searches:
        print(f"\nSearching for {search.keyword}, max price: {search.max_price}")

        listings = fetch_listings(search)

        for listing in listings:
            print(f"- {listing.title}: {listing.price} ({listing.url})")


if __name__ == "__main__":
    main()