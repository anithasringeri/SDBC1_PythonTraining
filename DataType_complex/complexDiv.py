#Example 4: Division with complex numbers
# Objective: Divide two complex numbers.
# Outcome: Prints a complex number result.
#Divide two complex numbers

a=7+3j
b=2+1j
result=a/b
print(result)
if result.imag>0:
    print("Division Result:", result)
else:
    print("Imaginary part non-positive")