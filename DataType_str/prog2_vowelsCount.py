# #Example 2: Counting vowels in a string
# #objective: Use for-else to count vowels.
# Outcome: Prints “Number of vowels: 3.”

#count vowels in a String

text="hell world Anitha"

vowels="aeiou"

count=0
for char in text:
    if char in vowels:
        count+=1
else:
    print("Number of Vowels:", count)