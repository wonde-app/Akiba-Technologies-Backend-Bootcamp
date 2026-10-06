
# Task 4: Temperature Station

# Celsius to Fahrenheit
# Get temperature from the user
celsius = float(input("Enter temperature in Celsius (°C): "))


# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Convert Celsius to Kelvin
kelvin = celsius + 273.15

print()
print("========== CELSIUS TO FAHRENHEIT ==========")
print(f"Celsius    : {celsius:.2f} °C")
print(f"Fahrenheit : {fahrenheit:.2f} °F")
print(f"Kelvin     : {kelvin:.2f} K")
print("============================================")

# Bonus: Fahrenheit to Celsius
fahrenheit_input = float(input("\nEnter temperature in Fahrenheit (°F): "))

celsius_from_fahrenheit = (fahrenheit_input - 32) * 5 / 9

print()
print("========== FAHRENHEIT TO CELSIUS ==========")
print(f"Fahrenheit : {fahrenheit_input:.2f} °F")
print(f"Celsius    : {celsius_from_fahrenheit:.2f} °C")
print("============================================")