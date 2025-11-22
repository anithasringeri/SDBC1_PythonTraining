# Example 5: Using tuple in a while loop
# Objective: Print items using while-else.
# Outcome: Prints all colors and “Finished printing colors.”

#print tuple item using while loop

colors=("red", "blue","green")
i=0
while i < len(colors):
    print("Color:" ,colors[i])
    i+=1
else:
    print("Finished printing colors.")

