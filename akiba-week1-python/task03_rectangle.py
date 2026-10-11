# Task 3: Rectangle Workshop

# Get rectangle dimensions
length = float(input("Enter the rectangle length (m): "))
width = float(input("Enter the rectangle width (m): "))

# Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Display the results
print()
print("=" * 50)
print("              RECTANGLE WORKSHOP")
print("=" * 50)

print(f"Length    : {length:.2f} m")
print(f"Width     : {width:.2f} m")
print(f"Area      : {area:.2f} m²")
print(f"Perimeter : {perimeter:.2f} m")

print("=" * 50)