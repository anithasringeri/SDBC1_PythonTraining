# Example 7: Simple interest calculation
# Objective: Calculate interest earned over time.
# Outcome: Prints interest earned: 50.0.

principal=1000.0
rate=5.0 #%
time=1.0 #year
interest=(principal*rate*time)/100
if interest > 0:
    print("Interest earned :", interest)
else:
    print("No Interest earned")