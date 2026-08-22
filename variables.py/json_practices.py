import json

data = {
    "name": "Sumaya",
    "role": "backend developer"
}

json_data = json.dumps(data)

print(json_data)