# Example 8: Complex number comparison by magnitude
# Objective: Find the largest magnitude.
# Outcome: Prints “Largest magnitude: (3+4j)”.

#find complex number with largest magnitude

complex_list=[2+3j, 3+4j,1+1j]
largest=complex_list[0]
for c in complex_list:
    if(c.real**2 + c.imag**2) > (largest.real**2 + largest.imag**2):
        largest=c
    else:
        print("Largest Magnitude:", largest)