[200~import requests

        def top_ten(subreddit):
            """Print the titles of the 10 hottest posts on a given subreddit."""
                # Construct the URL for the subreddit's hot posts in JSON format
                    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

                        # Define headers for the HTTP request, including User-Agent
                            headers = {
                                        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
                                            }

                                # Define parameters for the request, limiting the number of posts to 10
                                    params = {
                                                "limit": 10
                                                    }

                                        # Send a GET request to the subreddit's hot posts page
                                            response = requests.get(url, headers=headers, params=params)

                                                # Check if the subreddit exists
                                                    if response.status_code == 404:
                                                            print("Subreddit not found.")
                                                                    return

                                                                        # Parse the JSON response and extract the 'children' section
                                                                            data = response.json().get("data", {}).get("children", [])

                                                                                # Print the titles of the top 10 hottest posts
                                                                                    for post in data:
                                                                                            print(post["data"]["title"])

                                                                                            if __name__ == "__main__":
                                                                                                import sys
                                                                                                    if len(sys.argv) < 2:
                                                                                                            print("Please pass an argument for the subreddit to search.")
                                                                                                                else:
                                                                                                                        top_ten(sys.argv[1])

