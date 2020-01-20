import requests


page = requests.get("https://jsonplaceholder.typicode.com/posts")

response = page.json()
print(response[0]["title"])
