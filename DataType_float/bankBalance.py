# Example 4: Tracking a bank balance
# Objective: Deduct amounts until balance is below a threshold.
# Outcome: Prints each withdrawal and “Low balance warning.”

#deduct amounts until balance is low
"""

withdrawal=float(input("Enter Withdraw Amount :"))
balance=100.00
if withdrawal >= balance:
    print("Not sufficient balance, Your current balance is: ", balance)
else:
    while balance >20.0:
        print("Balance before withdrawal :", balance)
        balance-=withdrawal
        print("Current Balance:", balance)
        min_balance=balance
        if min_balance <=20:
            print("you need to maintain minimum balance of £20")
        else:
            continue
            
    else:
        print("Low balance warning. Final Balance:" ,  balance)

"""

withdrawal= 15.50
balance=100.00

while balance >= 20.0:
    print("Balance before withdrawal:", balance)
    balance-=withdrawal
else:
    print("Low balance warning. Final Balance:" ,  balance)
