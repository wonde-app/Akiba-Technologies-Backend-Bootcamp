# Task 7: Travel Planner

# Get travel information
distance = float(input("Enter the travel distance (km): "))
speed = float(input("Enter the average speed (km/h): "))

# Calculate travel time
time_hours = distance / speed

# Display travel information
print()
print("=" * 50)
print("                 TRAVEL PLANNER")
print("=" * 50)

print(f"Distance      : {distance:.2f} km")
print(f"Average Speed : {speed:.2f} km/h")
print(f"Travel Time   : {time_hours:.2f} hours")

print("=" * 50)