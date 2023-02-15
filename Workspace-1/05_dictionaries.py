person = {
    "name": "eren",
    "age": 21,
    "sex": "e",
    "hobbies": ["Basketball", "Software", "Game"],
}

print(person["name"])
print(person["age"])
print(person["sex"])
print(person["hobbies"])
print(person["hobbies"][0])
print(person["hobbies"][1])
print(person["hobbies"][2])


person["name"] = "Selin"
print(person["name"])

person.update({"name": "Eren", "age": 22})
print(person)

person["id"] = 909055
print(person)

del person["id"]
print(person)


for x in person:
    print(x)

for x in person:
    print(person[x])


print(person.keys())
print(person.values())
print(person.items())

for k in person.items():
    print(k)

for k, v in person.items():
    print(str(k) + ": " + str(v))


# print(person["id"]) # Error
print(person.get("id"))
print(person.get("id", "Bulunamadi"))

d = {k: v**2 for k, v in zip(["a", "b"], range(2))}
print(d)

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for item in d.items():
    print(item)


key_view = d.keys()
value_view = d.values()

print(key_view)
print(value_view)

d["c"] = 3
print(d)

print(key_view)
print(value_view)
