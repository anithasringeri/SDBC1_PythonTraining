# Example 5: Finding the maximum number
# Objective: Find the largest number using for-else.
# Outcome: Prints “Largest number: 42.”

# find the largest number

numbers=[10,42,5,8]
max_num=numbers[0]
for n in numbers:
    if n > max_num:
        max_num=n
else:
    print("Largest number:", max_num)

