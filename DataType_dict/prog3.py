# Example 3: Updating dictionary values
# Objective: Change value for an existing key.
# Outcome: Prints “Updated dictionary: {'item': 'book', 'price': 15}”.
# Update value in dictionary

item={"item":"book","price":10}
if "price" in item:
    item["price"]=15
    print("Updated dictionary:", item)
else:
    print("Price is missing")

