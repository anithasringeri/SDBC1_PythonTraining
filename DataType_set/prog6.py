# Example 6: Finding the intersection of sets
# Objective: Find elements common to both sets.
# Outcome: Prints {'banana'}.
#intersection of setscd 
set1={"apple", "banana"}
set2={"banana1", "cherry"}

common =set1 & set2
if common:
    print(common)
else: 
    print("No common elements")