# Example 6: Finding multiples of 3
# Objective: Print numbers divisible by 3 between 1 and 15.
# Outcome: Prints 3, 6, 9, 12, 15.

#print multiples of 3

for i in range(1,16):
    if i % 3==0:
        print(i)
else:
    print("All multiples of 3 printed")