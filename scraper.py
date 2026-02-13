"""
Amazon Product Scraper

Fetches a product page and extracts key details such as
title and price using requests and BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup

# Headers to mimic a real browser request
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/58.0.3029.110 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.5",
}


def get_product_details(product_url: str) -> dict:
    """
    Retrieves product title and price from an Amazon product page.

    Args:
        product_url (str): URL of the Amazon product.

    Returns:
        dict: Dictionary containing product title and price.
    """

    try:
        # Send HTTP request to product page
        response = requests.get(product_url, headers=headers)
        response.raise_for_status()

        # Parse HTML content
        soup = BeautifulSoup(response.content, "lxml")

        # Extract product title
        title = soup.find("span", {"id": "productTitle"}).get_text().strip()

        # Extract product price
        extracted_price = soup.find("span", {"class": "a-price"}).get_text().strip()
        price = "$" + extracted_price.split("$")[1]

        return {
            "title": title,
            "price": price,
        }

    except Exception as e:
        print("Error fetching product details.")
        print(f"Details: {e}")
        return {}


if __name__ == "__main__":
    product_url = input("Enter product URL: ")
    product_details = get_product_details(product_url)
    print(product_details)
