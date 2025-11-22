# Example 9: Filtering even numbers
# Objective: Extract even numbers using for-else.
# Outcome: Prints “Even numbers: [2, 4, 6]”.
#Filter  even numbers from a list

nums=[1,2,3,4,5,6]
print(type(nums))
evens=[]
for n in nums:
    if n % 2==0:
        evens.append(n)
else:
    print("Even Numbers:", evens)
