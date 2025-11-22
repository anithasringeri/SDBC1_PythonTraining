#Numeric Data Types
# exe4: Multiplication Table
#objective: Displays Multiplication table for a number


#outcome: prints the nx 1 to nX10
#slight modification asking user to Enter number, times table genrated for entered number

# Multication table
# Method1
"""
num=2
for i in range(1,11):
    print(num, 'X', i,'=',num*i)
else: 
    print("Times Table Completed")
"""

#Method 2 Using input functionality

num=int(input("Enter a number"))
for i in range(1,11):
    print(num, 'X', i,'=',num*i)
else: 
    print("Times Table Completed")