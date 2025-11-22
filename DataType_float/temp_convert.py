#Example 1: Converting Celsius to Fahrenheit
#Objective: Convert temperature using float arithmetic with if-else.
#Outcome: Prints “The temperature in Fahrenheit is 98.6.”

celsius= float(input("Enter temperatute in Celsius :"))
fahren=(celsius *9/5) + 32
if fahren > 98:
    print("The temperature in fahrenheit is", fahren)
else:
    print("Temperature is below normal")
