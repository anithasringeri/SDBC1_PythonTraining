# Example 10: Finding the key with the highest value
# Objective: Find the dictionary key with the highest value.
# Outcome: Prints “Top scorer: Bob with 92.”

# Find key with highest value
scores = {"Alice": 85, "Bob": 92, "Charlie": 88}
highest = list(scores.keys())[0]
for name in scores:
    if scores[name] > scores[highest]:
        highest = name
else:
    print("Top scorer:", highest, "with", scores[highest])

 