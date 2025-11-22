#Example 2: Rounding off a price
#Objective: Demonstrate rounding a float value.
#Outcome: Prints “Rounded price: 20.0.”

#Round off a float to the nearest whole number

price=float(input("Enter Amount :"))
#price=19.65
rounded_price=round(price)
if rounded_price>=price:
    print("Rounded Price:", rounded_price)
else: 
    print("Price rounded down")
