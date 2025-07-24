# main.py

def calc_after_tax(salary):
    # fixed ratio for tax calculation
    labor_insurance = salary * 0.08
    health_insurance = salary * 0.02
    pension = salary * 0.08           # the initial one is 0.06
    income_tax = salary * 0.05

    net_income = salary - (
        labor_insurance + health_insurance + pension + income_tax)
    return round(net_income, 2)

def show_menu():
    print("==== SalaryNet Calculator ====")
    try:
        salary = float(input("Enter your salary: "))
        result = calc_after_tax(salary)
        print(f"\nYour salary after tax is: {result}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for salary.")

if __name__ == "__main__":
    show_menu()
