salary = int(input("Enter your salary: "))

if salary < 30000:
    tax_rate = 5/100

elif 30000 <= salary <= 70000:
    tax_rate = 15/100

elif salary > 70000:
    tax_rate = 20/100

final_tax_rate = salary * tax_rate

print(f"Salary after {tax_rate * 100}% tax is {salary - final_tax_rate}")