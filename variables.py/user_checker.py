import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"
)

print("status:", response.status_code)

data = response.json()

print("name:", data["name"])
print("email:", data["email"])
print("city", data["address"]["city"])

try:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    response.raise_for_status()
    data = response.json()

    print("name:", data["name"])
    print("email:", data["email"])
    print("city", data["address"]["city"])

except requests.RequestException:
    print("something went wrong with the request.")