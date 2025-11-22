# Write a script to validate a password. 
# The validation rules are: at least 8 characters, 
# contains at least one uppercase letter, one lowercase letter, and one number. 
# Use a for loop to iterate through the characters of the password string 
# and if statements with boolean flags to check if all conditions are met.


password = input("Enter your password: ")
print(password)
has_upper = False
has_lower = False
has_digit = False


for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("Password is valid!")
else:
    print("Password is invalid.")
    print("Rules: At least 8 characters, 1 uppercase, 1 lowercase, and 1 number.")