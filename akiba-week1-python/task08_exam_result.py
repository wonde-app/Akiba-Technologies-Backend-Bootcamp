# Task 8: Exam Result Report

# Get student information
student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")

# Get exam marks
Python_score = float(input("Enter mark for Python_score: "))
English_score = float(input("Enter mark for English_score: "))
Mathematics_score = float(input("Enter mark for Mathematics_score: "))

# Calculate total and average
total_marks = Python_score + English_score + Mathematics_score
average_mark = total_marks / 3

# Display exam result
print()
print("=" * 50)
print("              EXAM RESULT REPORT")
print("=" * 50)

print(f"Student Name : {student_name}")
print(f"Student ID   : {student_id}")
print("-" * 50)

print(f"Python_score    : {Python_score:.2f}")
print(f"English_score    : {English_score:.2f}")
print(f"Mathematics_score    : {Mathematics_score:.2f}")

print("-" * 50)
print(f"Total Marks  : {total_marks:.2f}")
print(f"Average Mark : {average_mark:.2f}")

print("=" * 50)