 

# Example 9: Checking for empty range
# Objective: Determine if range(0) has any values.
# Outcome: Prints “Range is empty.”

 

# Check if range is empty
r = range(0)
print(r)
if len(r) == 0:
    print("Range is empty.")
else:
    print("Range has values.")