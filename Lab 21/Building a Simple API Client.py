import requests

class JSONPlaceholderClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.session = requests.Session()

    def get_posts(self):
        """Fetch all posts"""
        url = f"{self.BASE_URL}/posts"
        response = self.session.get(url)
        return response.json()

    def get_post(self, post_id):
        """Fetch a single post by ID"""
        url = f"{self.BASE_URL}/posts/{post_id}"
        response = self.session.get(url)
        return response.json()

    def create_post(self, title, body, user_id):
        """Create a new post"""
        url = f"{self.BASE_URL}/posts"
        payload = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        response = self.session.post(url, json=payload)
        return response.json()

# Example usage:
if __name__ == "__main__":
    client = JSONPlaceholderClient()

    print("Fetching posts...")
    posts = client.get_posts()
    print(posts[:2])  # print first 2 posts

    print("\nFetching post 1...")
    print(client.get_post(1))

    print("\nCreating a new post...")
    result = client.create_post("My Title", "This is the body", user_id=1)
    print(result)
