# Example 4: Counting occurrences of a number
# Objective: Count how many times 2 appears.
# Outcome: Prints “2 appears 3 times.”

#count the occurences of 2

num =[2,3,2,4,2]

count=0
for n in num:
    if n==2:
        count+=1
else:
    print("2 appears",count,"times")