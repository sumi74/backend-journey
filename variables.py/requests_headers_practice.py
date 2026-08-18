import requests

headers = {
    "user-agent": "backenddeveloper"
}

response = requests.get(
    "https://example.com",
    headers=headers
)

print("status:", response.status_code)
print("headers:", response.headers)