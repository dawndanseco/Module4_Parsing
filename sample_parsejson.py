import json

#example json
x = '{"name":"Dawn", "age":"22", "city": "Manila"}'

#parse json

y = json.loads(x)
print("The Output of the json file is", y)
print("Name:", y["name"])
print("Age:", y["age"])
print("City:", y["city"])