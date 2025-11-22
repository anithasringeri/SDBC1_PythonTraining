# Example 2: Accessing dictionary values
# Objective: Print value of a specific key.
# Outcome: Prints “Value for key 'name': Alice”.
# Access value by key

person={"name":"Alice", "age": 25}
if "name" in person:
    print("Value for key 'name':", person["name"])
else:
    print("Key not found")