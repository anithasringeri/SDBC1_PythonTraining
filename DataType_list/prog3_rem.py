# Example 3: Removing items from a list
# Objective: Remove items one by one using while-else.
# Outcome: Prints removed items and “All items removed.”

#Remove all items from the list

numbers=[1,2,3]
while numbers:
    removed = numbers.pop()
    print("Removed:", removed)
else:
    print("All items removed. List is empty:", numbers)