# Example 7: Iterating over key-value pairs
# Objective: Print all pairs using for-else.
# Outcome: Prints “Alice -> 85”, “Bob -> 90”, then “Iteration complete.”
# Iterate through dictionary items

grades= {"Alice": 85,"Bob":90, "Cat":38, "Dog": 50}
for name in grades:
    print(name, "-->", grades[name])
else:
    print("Iteration Complete.")



 