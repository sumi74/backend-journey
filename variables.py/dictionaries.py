student = {
    "name": "sumi",
    "age": 20,
    "country": "kenya"

}

print(student)
print(student["name"])
print(student["age"])
print(student["country"])

#
student["age"] = 21
student["city"] = "nairobi"

print(student)
print(student["age"])
print(student["city"])

#
student.pop("country")

print(student)

print(student.keys())
print(student.values())

print(student.items())