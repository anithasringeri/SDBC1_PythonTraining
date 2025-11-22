# Example 9: Creating a sequence of complex numbers
# Objective: Generate complex numbers with a pattern using while-else.
# Outcome: Prints numbers from (1+1j) to (5+5j).

#Generate a sequence of complex numbers

count=1
z = 1+1j
while count <= 5:
    print("Complex Number:", z)
    z=z+1+1j
    count+=1
else:
    print("Sequnence Genrated")