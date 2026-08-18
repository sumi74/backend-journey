import requests

params = {
    "name": "sumaya",
    "role": "backend_developer"
}
response = requests.get(
    "https://example.com",
    params=params
)

print("status:", response.status_code)
print("url:", response.url)