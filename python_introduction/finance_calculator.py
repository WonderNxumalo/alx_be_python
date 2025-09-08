monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
monthly_savings = float(monthly_income - monthly_expenses)

projected_savings = float((monthly_savings * 12) + (monthly_savings * 12 * 0.05))

print(f"""
      Enter your monthly income: {monthly_income}
      Enter your monthly expenses: {monthly_expenses}
      Your monthly savings are $ {monthly_savings}.
      Projected savings after one year, with interest, is: $ {projected_savings}.
      """)

""" /tmp/correction/7446214723889332675741141749742951659150_5/100739/921620/python_introduction/finance_calculator.py doesn't contain monthly_savings\s*=\s*(monthly_income\s*-\s*monthly_expenses|float\s*\(\s*monthly_income\s*\)\s*-\s*float\s*\(\s*monthly_expenses\s*\)) """
