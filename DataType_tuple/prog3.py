# Example 3: Tuple immutability
# Objective: Demonstrate that tuples cannot be changed.
# Outcome: Prints “Tuples are immutable.”

#Attempt to modify a tuple
colors=("red", "blue", "green")
try_index=1
if try_index < len(colors):
    print("Tuples are immutable. cannot change:", colors[try_index])
else:
    print("Index out of range")