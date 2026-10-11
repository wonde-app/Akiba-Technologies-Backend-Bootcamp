# Task 10: BMI Health Information

# Get user information
name = input("Enter your name: ")
weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

# Calculate BMI
bmi = weight / (height * height)

# Display BMI information
print()
print("=" * 50)
print("             BMI HEALTH INFORMATION")
print("=" * 50)

print(f"Name   : {name}")
print(f"Weight : {weight:.2f} kg")
print(f"Height : {height:.2f} m")
print(f"BMI    : {bmi:.2f} units")

print("=" * 50)