import requests

def get_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    response = requests.get(url)

    if response.status_code != 200:
       print("error:", response.status_code)
       return None

    return response.json()
