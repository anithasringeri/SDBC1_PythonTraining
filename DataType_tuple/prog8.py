# Example 8: Finding the largest number in a tuple
# Objective: Identify the largest number using for-else.
# Outcome: Prints “Largest number: 9.”
# Find the largest number
nums=(3,5,9,2)
largest=nums[0]
for n in nums:
    if n > largest:
        largest = n
    else:
        print("Largest number:", largest)

