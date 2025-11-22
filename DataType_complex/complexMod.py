# Example 6: Modulus of a complex number
# Objective: Find magnitude of a complex number.
# Outcome: Prints “Magnitude: 5.0.”

z=3+4j
magnitude=(z.real**2 + z.imag**2)**0.5
if magnitude == 5:
    print("Magnitude :",magnitude)
else:
    print("Different magnitude")