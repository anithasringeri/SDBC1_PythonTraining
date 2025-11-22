# Example 3: Reversing a string using while
# Objective: Reverse a string manually.
# Outcome: Prints “Reversed string: nohtyp”.

#Reverse the String using while loop

original="python"
reversed_text=""
i =len(original)-1
print(i)
while i>0:
    reversed_text+=original[i]
    i-=1
else:
    print("Reversed string:", reversed_text)