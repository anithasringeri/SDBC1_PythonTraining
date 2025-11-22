# Example 6: Sorting a list manually
# Objective: Sort numbers using while loop.
# Outcome: Prints “Sorted list: [1, 2, 3, 4]”.

#sort list manually 
nums=[4,2,3,1]
sorted_list=[]
while nums:
    smallest=nums[0]
    for n in nums:
        if n < smallest:
            smallest= n
        nums.remove(smallest)
        sorted_list.append(smallest)
    else:
        print("Sorted list:", sorted_list)
        