#Example 10: Factorial calculation
#Objective: Calculate factorial using while.
#Outcome: Prints factorial of 5.

num=int(input("Enter a number "))
fact=1

while num >0:
    fact*=num
    num-=1
    #print("Num :",num, "fact :" fact)
else:
    print("The factorial of given number is :", fact)


