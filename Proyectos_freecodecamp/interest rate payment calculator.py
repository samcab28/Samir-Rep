#monthly payment loan calculator
def main():
    principal = float(input('enter the load amount: '))
    apr = float(input("input annual interest rate: "))
    years = int(input('input ammount of years: '))

    monthly_intererst_rate = apr/1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_intererst_rate / (1-(1+monthly_intererst_rate)**(-amount_of_months))

    print(monthly_payment)

while True: 
    main()