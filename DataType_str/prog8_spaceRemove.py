# Example 8: Removing spaces from a string
# Objective: Use while-else to remove all spaces.
# Outcome: Prints “String without spaces: HelloWorld”.
#Remove spaces from a string

text="Hello World"
result=""
i=0
while i < len(text):
    if text[i]!=" ":
        result+=text[i]
        #print(result)
    i+=1   
else:
    print("String without spaces:", result)
