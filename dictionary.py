empty_dict = {}
a = { "one": 1, "two": 2, "three": 3 }
print(a["one"])

print(a.keys())
print(a.values())
print(a.items())

a.update({"four": 4})
print(a.items())
