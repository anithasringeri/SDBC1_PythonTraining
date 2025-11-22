# Example 1: Adding two complex numbers
# Objective: Perform addition with complex numbers.
# Outcome: Prints “Sum: (5+8j)”.

#Add 2 complex number type <class Complex>
a=3+4j   # can also be assigned as a= complex(3,4) b=complex(5,-2)
b=2-4j
# a=complex(3,4) 
# b=complex(5,-2)
sum_complex=a+b
if sum_complex.imag >0:
    print("Sum:", sum_complex)
else:
    print("No imaginary Part")