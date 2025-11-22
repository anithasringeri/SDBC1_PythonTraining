# Example 9: Converting string to uppercase
# Objective: Convert text to uppercase if not already.
# Outcome: Prints “Converted text: HELLO”.

s="hello"
if s.isupper():
    print("Already uppercase", s)
else:
    print("Convert text:", s.upper())