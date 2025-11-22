# Example 7: Difference between two sets
# Objective: Find elements in one set but not the other.
# Outcome: Prints {'apple'}.
# Difference between two sets
set1 = {"apple", "banana", "cat","dog"}
set2 = {"banana", "cherry"}
diff=set1-set2
if diff:
    print(diff)
else:
    print("No difference found.")
