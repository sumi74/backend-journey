import requests


def get_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        response = requests.get(url)
    except requests.RequestException:
        print("Network error. Please check your internet connection.")
        return None

    if response.status_code != 200:
        print("error:", response.status_code)
        return None

    return response.json()


def create_user(name, email, city):
    url = "https://jsonplaceholder.typicode.com/users"

    data = {
        "name": name,
        "email": email,
        "address": {
            "city": city
        }
    }

    response = requests.post(url, json=data)

    return response


def update_user(user_id, name, email, city):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    data = {
        "name": name,
        "email": email,
        "address": {
            "city": city
        }
    }

    response = requests.put(url, json=data)

    return response


def delete_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    response = requests.delete(url)

    return response

