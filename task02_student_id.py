# Task 2: Student ID Card

# Get student information
student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")
department = input("Enter department: ")
year = int(input("Enter year: "))
university = input("Enter university: ")
phone_number = input("Enter phone number: ")

# Display student ID card
print()
print("+" + "-" * 48 + "+")
print("|" + "STUDENT ID CARD".center(48) + "|")
print("+" + "-" * 48 + "+")
print(f"| Student Name : {student_name:<32} |")
print(f"| Student ID   : {student_id:<32} |")
print(f"| Department   : {department:<32} |")
print(f"| Year         : {year:<32} |")
print(f"| University   : {university:<32} |")
print(f"| Phone Number : {phone_number:<32} |")
print("+" + "-" * 48 + "+")