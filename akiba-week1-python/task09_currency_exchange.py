# Task 9: Currency Exchange Desk

# Exchange rate
USD_TO_ETB = 150.00

# Get amount from the user
usd_amount = float(input("Enter amount in USD ($): "))

# Convert USD to Ethiopian Birr
etb_amount = usd_amount * USD_TO_ETB

# Display the result
print()
print("=" * 50)
print("             CURRENCY EXCHANGE DESK")
print("=" * 50)

print(f"Exchange Rate : 1 USD = {USD_TO_ETB:.2f} ETB")
print(f"USD Amount    : {usd_amount:.2f} USD")
print(f"ETB Amount    : {etb_amount:.2f} ETB")

print("=" * 50)