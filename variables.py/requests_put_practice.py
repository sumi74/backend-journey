import requests

data = {
    "title": "backend developer",
    "body": "i am learning python",
    "userId": 1
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=data
)

print("status:", response.status_code)
print("updated:", response.json())
