""" bank loan calculator"""
def calculate_emi(principal, annual_rate, tenure_months):
    if annual_rate == 0:
        emi = principal / tenure_months
    else:
        r = annual_rate / 12 / 100
        n = tenure_months
        emi = principal * r * ((1 + r) ** n )/ (((1 + r) ** n) - 1)
    return round (emi, 2)

def calculate_total_payable(emi, tenure_months):
    return round(emi * tenure_months, 2)

def calculate_total_interest(total_payable, principal):
    return round(total_payable - principal, 2)

def check_eligiblity(emi, monthly_income):
    max_allowed_emi = round(0.40 * monthly_income, 2)
    is_eligible = emi <= max_allowed_emi
    return is_eligible, max_allowed_emi

def main():
    try:
        principal = float(input("enter principal amount:"))
        if principal <= 0:
            print("invalid loan amount. enter a positive number")
            return
        annual_rate = float(input("enter annual interest rate(0 to 30%):"))
        if annual_rate < 0 or annual_rate > 30:
            print("invalid interst rate. enter a rate between 0 and 30.")
            return
        tenure_months = int(input("enter tenure (in months, 1 to 360):"))
        if tenure_months < 1 or tenure_months > 360 :
            print("invalid tenure. enter tenure between 1 to 360 months.")
            return
        monthly_income_str = input("enter monthly income: ").strip()
        if not monthly_income_str:
            return
        monthly_income = float(monthly_income_str)
        if monthly_income <= 0:
            print("invalid monthly income. enter a positive income.")
            return
    except ValueError:
        print("invalid input. please enter a valid input.")

    emi = calculate_emi(principal, annual_rate, tenure_months)
    total_payable = calculate_total_payable(emi, tenure_months)
    total_interest = calculate_total_interest(total_payable, principal)
    is_eligible ,max_allowed_emi = check_eligiblity(emi, monthly_income)

    if is_eligible:
        print(f"EMI: Rs. {emi:.2f} | Total Payable: Rs. {total_payable:.2f}")
        print(f"Total Interest: Rs. {total_interest:.2f} | Eligible: Yes")
    else:
        print(f"EMI: Rs. {emi:.2f}")
        print(f"Maximum allowed EMI (40% of income): Rs. {max_allowed_emi:.2f}")
        print("Loan not eligible: EMI exceeds the allowed limit.")

if __name__ == "__main__":
    main()
