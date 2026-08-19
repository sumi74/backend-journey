import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"

)

print("status:", response.status_code)
data = response.json()

print("name:", data["name"])
print("email:", data["email"])
print("city:", data["address"]["city"])
