# main.py

def calc_after_tax(salary):
    # fixed ratio for tax calculation
    labor_insurance = salary * 0.08
    health_insurance = salary * 0.02
    pension = salary * 0.06
    income_tax = salary * 0.05

    net_income = salary - (
        labor_insurance + health_insurance + pension + income_tax)
    return round(net_income, 2)

if __name__ == "__main__":
    salary = float(input("Enter your salary: "))
    net = calc_after_tax(salary)
    print(f"Your salary after tax is: {net}")