#Example 1: Adding items to a shopping list
# Objective: Use a list to store items and add until limit is reached.
# Outcome: Prints items added and “Shopping list complete.”

#Adding items to a shopping List
shopping_list=[]
items=["Milk", "bread","butter","apple","banana"]
i=0
while i < len(items):
    shopping_list.append(items[i])
    print("Added:",items[i])
    i+=1
else:
    print("Shopping list complete:", shopping_list)
