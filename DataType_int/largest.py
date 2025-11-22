#Example 6: Find the largest number
#Objective: Use integers with if to find the largest in a list.
#Outcome: Prints the largest number.
#exe6: Largest Number

numbers=[5,9,2,10,3]
largest = numbers[0]
#print(largest)
for i in numbers:
    #print("i :",i)
    if i > largest:
        largest = i

print("The largest number is :", largest)
