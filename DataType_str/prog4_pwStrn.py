# Example 4: Checking password strength
# Objective: Evaluate password with if-elif-else.
# Outcome: Prints “Strong password.”

#check password strenght

password="Python123"
if len(password) < 6:
    print("weak password")
elif password.isalnum() and any(ch.isdigit() for ch in password):
    print("Strong password")
else:
    print("Password needs numbers and letter")