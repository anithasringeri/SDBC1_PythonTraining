# Example 10: Building a list of squares
# Objective: Generate squares of numbers using while-else.
# Outcome: Prints “Squares: [1, 4, 9, 16, 25]”.

# Generate squares of numbers 1 to 5

squares=[] # crate empty list
n=1
while n <= 5:
    squares.append(n*n)
    n+=1
else:
    print("Squares:", squares)