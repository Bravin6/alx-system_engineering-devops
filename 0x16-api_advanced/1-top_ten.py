 #!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 404:
        print("Subreddit not found.")
        return
    results = response.json().get("data")
    for post in results.get("children", []):
        print(post.get("data").get("title"))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

