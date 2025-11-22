#Example 8: Simple ATM withdrawal
#Objective: Deduct money using while-else.
#Outcome: Prints balance after withdrawals.

balance=50
withdraw=10
while balance>=withdraw :
    print("withdrawing", withdraw)
    balance-=withdraw
    print("Remaining Balance:", balance)

print("No more funds")