monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
monthly_savings = float(monthly_income - monthly_expenses)

projected_savings = ((monthly_savings * 12) + (monthly_savings * 12 * 0.05))

print(f"""
      Enter your monthly income: {monthly_income}
      Enter your monthly expenses: {monthly_expenses}
      Your monthly savings are $ {monthly_savings}.
      Projected savings after one year, with interest, is: $ {projected_savings}.
      """)
monthly_savings = float(monthly_income) - float(monthly_expenses)
