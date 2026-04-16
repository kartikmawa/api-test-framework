import requests

def get_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    return requests.get(url)