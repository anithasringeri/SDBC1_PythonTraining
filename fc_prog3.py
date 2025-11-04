# Write a script that iterates through a 
# list of dictionaries (e.g., student records) and 
# uses a for loop and an if statement to find and 
# print the name of the student with the highest score.

students = [
    {"name": "Ashli", "score": 85},
    {"name": "Alex", "score": 90},
    {"name": "Ralph", "score": 75},
    {"name": "David", "score": 65},
    {"name": "Jhon", "score": 96} 

]
highest_score = 0
top_student = ""

for student in students:
    if student["score"] > highest_score:
        highest_score = student["score"]
        top_student = student["name"]
print("Top scoring student is:", top_student)


