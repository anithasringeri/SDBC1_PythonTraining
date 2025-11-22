# Example 7: Iterating through a list of complex numbers
# Objective: Print real and imaginary parts using for-else.
# Outcome: Prints parts of each complex number, then “All numbers printed.”

#iterate through comple numbers
numbers=[1+2j, 3+4j, 5+6j]
for n in numbers :
    print("Real:", n.real, "| Imaginary:", n.imag)
else:
    print("All Numbers printed")