# Task 5: Ethiopian Shopping Receipt

# Get item information
item1_name = input("Enter the first item name: ")
item1_quantity = int(input("Enter the quantity: "))
item1_price = float(input("Enter the unit price (ETB): "))

item2_name = input("\nEnter the second item name: ")
item2_quantity = int(input("Enter the quantity: "))
item2_price = float(input("Enter the unit price (ETB): "))

item3_name = input("\nEnter the third item name: ")
item3_quantity = int(input("Enter the quantity: "))
item3_price = float(input("Enter the unit price (ETB): "))

# Calculate the cost of each item
item1_total = item1_quantity * item1_price
item2_total = item2_quantity * item2_price
item3_total = item3_quantity * item3_price

# Calculate the overall total
grand_total = item1_total + item2_total + item3_total

# Display the shopping receipt
print()
print("=" * 60)
print("               ETHIOPIAN SHOPPING RECEIPT")
print("=" * 60)

print(f"{'Item':<20}{'Qty':>8}{'Unit Price':>14}{'Total':>14}")
print("-" * 60)

print(f"{item1_name:<20}{item1_quantity:>8}{item1_price:>14.2f}{item1_total:>14.2f}")
print(f"{item2_name:<20}{item2_quantity:>8}{item2_price:>14.2f}{item2_total:>14.2f}")
print(f"{item3_name:<20}{item3_quantity:>8}{item3_price:>14.2f}{item3_total:>14.2f}")

print("-" * 60)
print(f"{'GRAND TOTAL':<46}{grand_total:>14.2f} ETB")
print("=" * 60)