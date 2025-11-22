# Example 8: Merging two dictionaries
# Objective: Combine values of two dictionaries manually.
# Outcome: Prints “Merged dictionary: {'a': 1, 'b': 2, 'c': 3}”.
#merge two dictionaries manually

d1={"a":1, "b":2}
d2={"c":3}
for key in d2:
    d1[key]=d2[key]
else:
    print("Merged Dictionary:",d1)