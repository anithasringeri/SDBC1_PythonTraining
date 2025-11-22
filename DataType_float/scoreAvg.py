# #Example 3: Average of test scores
# #Objective: Compute the average using floats with for-else.
# Outcome: Prints “Average score: 82.5.”
# calculate average of testscores

scores=[80.5,90.0,75.5]
total=0.0
for score in scores:
    total+=score
    print(total)
else:
    averge=total/len(scores)
    print("Averge score :" , averge)
