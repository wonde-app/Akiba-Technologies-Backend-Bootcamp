
# Task 1: Even or Odd Number Checker

# Step 1: Get an integer from the user
number = int(input("Enter an integer: "))

# Step 2: Check whether the number is even or odd
if number % 2 == 0:
    result = "Even"
else:
    result = "Odd"

print("\n========== EVEN OR ODD CHECKER ==========")
print(f"Number: {number}")
print(f"Result: {result}")
print("=========================================")
