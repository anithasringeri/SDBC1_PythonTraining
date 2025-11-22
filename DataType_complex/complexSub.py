#Example 2: Subtracting complex numbers
# Objective: Demonstrate subtraction of complex numbers.
# Outcome: Prints “Difference: (1+0j)”.
#subtract two complexnnumbers

x=5+3j   # can also be assigned as a= complex(3,4) b=complex(5,-2)
y=4+3j

difference=x-y
if difference.real >0:
    print("Difference:", difference)
else:
    print("Negative or zero part.")
