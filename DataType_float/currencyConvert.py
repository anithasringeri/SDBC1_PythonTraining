# Example 10: Currency conversion
# Objective: Convert USD to EUR using floats and for-else.
# Outcome: Prints conversion for 1–5 USD.

#convert USD to EUR

rate=0.92 #conversion rate
for i in range(1,6):
    eur=i * rate
    print(i,"USD=" ,round(eur,2) ,"EUR")
else:
    print("Conversion completed")
    