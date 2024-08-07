students_ages = {
    'Alice': 20,
    'Bob': 22,
    'Charlie': 19,
    'Diana': 21,
    'Eve': 23
}

student_name = 'Charlie'
print(f"The age of {student_name} is: {students_ages[student_name]}")
students_ages['Frank'] = 24
print("Updated dictionary with new student:")
print(students_ages)

