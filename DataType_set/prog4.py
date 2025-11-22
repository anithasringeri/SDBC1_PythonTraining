# Example 4: Removing elements from a set
# Objective: Remove elements one by one using while-else.
# Outcome: Prints “All items removed. Set is empty.”
# Remove all elements from a set
colors = {"red", "blue"}
while colors:
    colors.pop()
else:
    print("All items removed. Set is empty")
print(colors)
