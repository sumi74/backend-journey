import requests

response = requests.delete(
    "https://jsonplaceholder.typicode.com/posts/1"
)

print("status", response.status_code)
print("response:", response.text)