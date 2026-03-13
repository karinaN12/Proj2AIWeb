import requests

API_KEY = "AIzaSyCzJUyVAQkxYkc-z_WcqK-6tXy7NzBV4V0"
SEARCH_ENGINE_ID = "a66bf15d1597d421d"
SEARCH_URL = "https://www.googleapis.com/customsearch/v1"


def search_web(query):
    params = {
        "key": API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": query,
        "num": 5
    }

    response = requests.get(SEARCH_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def print_results(data):
    items = data.get("items", [])

    if not items:
        print("No results found.")
        return

    print("\nSearch Results:\n")
    for i, item in enumerate(items, start=1):
        title = item.get("title", "No title")
        link = item.get("link", "No URL")
        snippet = item.get("snippet", "No snippet")

        print(f"Result {i}")
        print(f"Title: {title}")
        print(f"URL: {link}")
        print(f"Snippet: {snippet}")
        print("-" * 50)


def main():
    query = input("Enter a search query: ").strip()

    if not query:
        print("No query entered.")
        return

    if not API_KEY or not SEARCH_ENGINE_ID:
        print("Missing API_KEY or SEARCH_ENGINE_ID.")
        return

    try:
        data = search_web(query)
        print_results(data)
    except requests.exceptions.RequestException as e:
        print(f"Error performing web search: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
