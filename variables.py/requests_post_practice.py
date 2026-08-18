import requests

data = {
    "name": "sumaya",
    "role": "backend developer"
}

response = requests.post(
    "https://htpbin.org/post",
    json=data
)

print("status:", response.status_code)
print("response:", response.json())
