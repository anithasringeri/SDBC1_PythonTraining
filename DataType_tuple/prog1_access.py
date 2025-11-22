#Tuples are Ordered, immutable collections used to store multiple items in a single variable
# ordered : items in a tuple maintain their position and can be accessed via indexing
#Immutable : once created the contents of a tuple cannot be changed - no adding, removing or modifying elements
#Allow duplicates:Tuples can contain repeated values
#Hetrogeneous: you can mix data types - integer, string, list etc with in single tuple
# created using () 
#count() and index() built-in function
# len(t) – Returns the number of elements.
# max(t) / min(t) – Returns the largest/smallest item.
# sum(t) – Returns the sum of all numeric elements.
# sorted(t) – Returns a sorted list from the tuple.
# reversed(t) – Returns a reverse iterator.

# Example 1: Accessing elements of a tuple
# Objective: Print each item in a tuple using for-else.
# Outcome: Prints all fruits and “All items printed.”

#Access each item in a tuple

fruits=("apple","banana", "cherry")
for fruit in fruits:
    print("Fruit:", fruit)
else: 
    print("All items printed")