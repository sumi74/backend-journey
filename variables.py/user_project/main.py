from utils import greet, show_user
from models import user

user = user("sumaya", "sumaya@example.com")

print(greet(user.name))
show_user(user)
