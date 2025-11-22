# Example 4: Deleting dictionary keys
# Objective: Remove keys using while-else.
# Outcome: Prints “All keys removed. {}”.

#Remove all keys from dictionary
#d={}
d={"a":1,"b":2}
while d:
    key=list(d.keys())[0]
    print("Now Key has:", key)
    del d[key]
else:
    print("All keys are removed", d)