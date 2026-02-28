import json

# 1. Python to JSON
data = {"name": "Ali", "age": 20}
j = json.dumps(data)
print(j)

# 2. JSON to Python
p = json.loads(j)
print(p)

# 3. Write JSON file
with open("data.json", "w") as f:
    json.dump(data, f)

# 4. Read JSON file
with open("data.json", "r") as f:
    d = json.load(f)
    print(d)

# 5. JSON with list
data2 = {"students": ["Ali", "Aruzhan", "Dias"]}
print(json.dumps(data2)) 