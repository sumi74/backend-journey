with open("data.txt", "w") as file:
    file.write("i am learning python")

with open("data.txt", "a") as file:
    file.write("\nl am becoming backend developer")

with open("data.txt", "r") as file:
    content = file.read()
    print(content)