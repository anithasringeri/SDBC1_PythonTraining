#Example 10: Tuple unpacking
# Objective: Assign tuple values to variables.
# Outcome: Prints “Name: John, Age: 25, City: London.”
#unpack tuple values
person =("John", 25, "London")
if len(person) == 3:
    name, age, city=person
    print("Name:", name,"Age:",age,"City:", city)
else:
    print("Tuple does not have exactly 3 elemets.")


