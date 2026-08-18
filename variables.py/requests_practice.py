import requests
response = requests.get("https://example.com")
print("status:", response.status_code)
print("url:", response.url)
print("content:", response.text[:100])