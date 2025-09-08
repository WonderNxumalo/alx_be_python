income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your monthly expenses: "))
savings = income - expenses

projected_savings = (savings * 12) + (savings * 12 * 0.05)

print(f"""
      Enter your monthyl income: {income}
      Enter your monthly expenses: {expenses}
      Your monthly savings are $ {savings}.
      Projected savings after one year, with interest, is: $ {projected_savings}.
      """)