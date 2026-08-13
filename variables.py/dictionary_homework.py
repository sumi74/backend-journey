person = {
    "name": "ali",
    "age": 25,
    "city": "nairobi"
}

print(person["name"])
print(person["age"])

person["job"] = "developer"
person["age"] = 26

print(person)

person.pop("city")

print(person)