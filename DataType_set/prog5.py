# Example 5: Finding the union of two sets
# Objective: Combine two sets into one.
# Outcome: Prints {'apple', 'banana', 'cherry', 'orange'}.
set1={"apple", "banana"}
set2 = {"cherry", "banana", "orange"}
union_set= set1|set2
if len(union_set)==4:
    print(union_set)
else:
    print("Union size mismatch")