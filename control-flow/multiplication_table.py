number = int(input("Enter a number to see its multiplication table: "))

multipliers = range(1,11)

for multiplier in multipliers:
    product = number * multiplier
    print(f"{number} * {multiplier} = {product}")
    