#Example 7: Counting occurrences
#Objective: Count how many times 3 appears.
#Outcome: Prints “3 appears 2 times.”

count=0
num=[1,0,5,9,1,10,13]
for i in num:
    if i==3:
        count+=1
print("Number of time 3 appear :" , count)

