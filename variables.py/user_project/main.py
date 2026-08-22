from models import user
from utils import get_user

user_id = int(input("enter user id: "))
data = get_user(user_id)

if data:
    user = user(
        data["name"],
        data["email"],
        data["address"]["city"]

    )

    user.show_info()