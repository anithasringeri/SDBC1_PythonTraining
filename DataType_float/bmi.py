# Example 6: Calculating BMI
# Objective: Use floats in BMI calculation and if-elif.
# Outcome: Prints “Normal weight.”

weight=73 #kg
height=1.75 #meters
bmi=weight/height*height
if bmi < 18.5:
    print("Under weight")
elif bmi < 25:
    print("Normal Weight")
else:
    print("Over weight")


