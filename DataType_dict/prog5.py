# Example 5: Counting items in a dictionary
# Objective: Count total key-value pairs.
# Outcome: Prints “Number of entries: 3.”
#Count number of items in dictionary

d={"x": 10, "y":20, "z":30}

count=0
for key in d:
    count+=1
else:
    print("Number of entries:", count)
    