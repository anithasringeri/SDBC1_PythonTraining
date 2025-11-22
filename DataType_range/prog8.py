# Example 8: Using range() in a while loop
# Objective: Iterate over range manually.
# Outcome: Prints values 0 to 4, then “Iteration complete.”

 

# Use range in a while loop

r=range(5)
i=0
while i < len(r):
    print(r[i])
    i+=1
else:
    print("iteration complete")