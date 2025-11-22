# Example 4: Nested tuple access
# Objective: Access elements inside nested tuples.
# Outcome: Prints “Nested element: 3.”

# Access elements in nested tuples

nested =(1,2,(3,4))
if isinstance(nested[2], tuple):
    print("Nested element:" , nested[2][0])
else:
    print("No nested tuple found.")
