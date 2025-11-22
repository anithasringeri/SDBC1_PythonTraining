#Numeric Data Types
# exe1: Counting down a timer
#objective: Use an integer to count down with while-else.
#outcome: prints numbers 5 to 1 then "Timer complete!"

timer =5
while timer > 0:
    print("Time Left:", timer)
    timer-=1
else:
    print("Timer Completed!")