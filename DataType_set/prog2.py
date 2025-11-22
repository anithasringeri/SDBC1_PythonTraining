# Example 2: Adding elements to a set
# Objective: Add new elements one by one using while-else.
# Outcome: Prints “Final set: {1, 2, 3}”.

numbers=s()
to_add=[1,2,3]
i=0
while i < len(to_add):
    numbers.add(to_add[i])
    i+=1
else:
    print("Final set:", numbers)