# Example 5: Checking if a complex number is purely real
# Objective: Use if-else to check imaginary part.
# Outcome: Prints “Number has no imaginary part.”

# check if number is purely real
z=10+0j
if z.imag==0:
    print("Number has no imaginary part")
else:
    print("Number has imaginary part")