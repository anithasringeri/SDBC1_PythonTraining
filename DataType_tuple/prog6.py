# Example 6: Counting elements in a tuple
# Objective: Count occurrences of “apple.”
# Outcome: Prints “Apple occurs 2 times.”

 # Count how many times 'apple' occurs
fruits = ("apple", "banana", "apple", "cherry")
count = 0
for fruit in fruits:
    if fruit == "apple":
        count += 1
else:
    print("Apple occurs", count, "times.")