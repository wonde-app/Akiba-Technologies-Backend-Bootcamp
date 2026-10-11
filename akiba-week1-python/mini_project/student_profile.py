# Mini Project: Student Profile System

# ==========================================
# 1. GET STUDENT INFORMATION
# ==========================================

full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
university = input("Enter your university: ")
department = input("Enter your department: ")
favorite_language = input("Enter your favorite programming language: ")
programming_goal = input("Enter one programming goal: ")


# ==========================================
# 2. DISPLAY STUDENT PROFILE
# ==========================================

print()
print("=" * 60)
print("                  STUDENT PROFILE")
print("=" * 60)

print(f"Full Name                : {full_name}")
print(f"Age                      : {age}")
print(f"City                     : {city}")
print(f"University               : {university}")
print(f"Department               : {department}")
print(f"Favorite Language        : {favorite_language}")
print(f"Programming Goal         : {programming_goal}")

print("=" * 60)
print("              PROFILE CREATED SUCCESSFULLY")
print("=" * 60)