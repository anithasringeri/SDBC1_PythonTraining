# Example 6: Checking if a value exists
# Objective: Verify if a value exists in dictionary.
# Outcome: Prints “Value found.”

#check if value exist

score={"Alice": 85,"Bob":90, "Cat":38, "Dog": 50}
#if  "Alice" in score.keys():
if  50 in score.values():
    print("Value found")
else:
    print("Value not found")