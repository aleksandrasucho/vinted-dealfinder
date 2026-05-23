from vinted_deal_finder.models import Listing, SearchRule


def fetch_listings(search: SearchRule) -> list[Listing]:
    fake_listings = [
        Listing(
            id="vinted-1",
            title=f"{search.keyword} in black",
            price=search.max_price - 2,
            url="https://www.vinted.co.uk/",
        ),
        Listing(
            id="vinted-2",
            title=f"Expensive {search.keyword}",
            price=search.max_price + 20,
            url="https://www.vinted.co.uk/",
        ),
    ]

    return [
        listing
        for listing in fake_listings
        if listing.price <= search.max_price
    ]