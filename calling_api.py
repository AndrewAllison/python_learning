import json

import requests


def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        return posts
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")
        return None


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))


def main():
    print("Fetching posts from JSONPlaceholder API...")
    posts = fetch_posts()
    if posts:
        print("Successfully fetched posts! Here is the pretty-printed JSON:")
        pretty_print_json(posts[:5])  # Print the first 5 posts in a nicely formatted way


if __name__ == "__main__":
    main()
