# Example 8: Reversing a list
# Objective: Reverse a list manually.
# Outcome: Prints “Reversed list: [4, 3, 2, 1]”.

#reverse a list manually

original = [1,2,3,4]

reverse_list=[]
i=len(original)-1
print(i)
while i>=0 :
    reverse_list.append(original[i])
    i-=1
else:
    print("Reversed list:", reverse_list)