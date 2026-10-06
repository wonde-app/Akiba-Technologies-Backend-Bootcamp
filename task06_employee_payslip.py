# Task 6: Employee Payslip

# Get employee information
employee_name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")

# Get salary information
basic_salary = float(input("Enter basic salary (ETB): "))
allowance = float(input("Enter allowance (ETB): "))
bonus = float(input("Enter bonus (ETB): "))

# Calculate gross salary
gross_salary = basic_salary + allowance + bonus

# Calculate tax
tax_rate = 0.10
tax = gross_salary * tax_rate

# Calculate net salary
net_salary = gross_salary - tax

# Display payslip
print()
print("=" * 55)
print("                 EMPLOYEE PAYSLIP")
print("=" * 55)

print(f"Employee Name : {employee_name}")
print(f"Employee ID   : {employee_id}")
print("-" * 55)

print(f"Basic Salary  : {basic_salary:,.2f} ETB")
print(f"Allowance     : {allowance:,.2f} ETB")
print(f"Bonus        : {bonus:,.2f} ETB")
print(f"Gross Salary  : {gross_salary:,.2f} ETB")
print(f"Tax (10%)     : {tax:,.2f} ETB")
print(f"Net Salary    : {net_salary:,.2f} ETB")

print("=" * 55)