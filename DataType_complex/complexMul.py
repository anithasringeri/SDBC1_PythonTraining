# Example 3: Multiplying complex numbers
# Objective: Multiply two complex numbers.
# Outcome: Prints “Product: (-7+22j)”.

num1= 3+4j
num2= 2+5j

product=num1 * num2
if product.real<0:
    print("Product: ",product)
else:
    print("Real part is non Negative.")

