from vinted_deal_finder.config import load_searches
from vinted_deal_finder.fetcher import fetch_listings
from vinted_deal_finder.storage import load_seen_listing_ids, save_seen_listing_ids


SEEN_LISTINGS_PATH = "backend/data/seen_listings.json"


def main() -> None:
    searches = load_searches("backend/config/searches.json")
    seen_listing_ids = load_seen_listing_ids(SEEN_LISTINGS_PATH)

    print("Vinted Deal Finder backend is running.")
    print(f"Loaded {len(searches)} searches:")

    for search in searches:
        print(f"\nSearching for {search.keyword}, max price: {search.max_price}")

        listings = fetch_listings(search)
        new_listings = [
            listing
            for listing in listings
            if listing.id not in seen_listing_ids
        ]

        for listing in new_listings:
            print(f"- NEW: {listing.title}: {listing.price} ({listing.url})")
            seen_listing_ids.add(listing.id)

    save_seen_listing_ids(SEEN_LISTINGS_PATH, seen_listing_ids)


if __name__ == "__main__":
    main()