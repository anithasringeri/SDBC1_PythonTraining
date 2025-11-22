# Dictionary (dict)
# Example 1: Adding key-value pairs
# Objective: Create a dictionary and add items using while-else.
# Outcome: Prints “Dictionary filled: {'a': 1, 'b': 2, 'c': 3}”.

#creating a dictionary and add key-value pair

data={}
print(type(data))
keys=['a','b','c']
values=[1,2,3]
i=0
while i < len(keys):
    data[keys[i]] = values[i]
    print(data)
    print(type(data))

    i+=1
else:
    print("Dictionary filled:", data)