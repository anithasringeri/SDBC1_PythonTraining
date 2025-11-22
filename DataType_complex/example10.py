# Example 10: Checking if imaginary part is greater than real part
# Objective: Compare real and imaginary parts.
# Outcome: Prints messages for each comparison.

#Compare real and imaginary parts

values=[2+3j, 4+2j, 1+5j]
for v in values:
    if v.imag > v.real:
        print(v, "-Imaginary part is greater.")
    elif v.imag == v.real:
        print(v, "-Real and imaginary are equal.")
    else:
        print(v,"- Real part is greater")
else: 
    print("Comparision Compelete")
