input = input(f"What's the weather like today? (sunny/rainy/cold): ")

if input.lower() == 'sunny':
    print(f"Wear a t-shirt and sunglasses.")
elif input.lower() == 'rainy':
    print(f"Don't forget your umbrella and a raincoat.")
elif input.lower() == 'cold':
    print(f"Make sure to wear a warm coat and a scarf.")
else: 
    print(f"Sorry, I don't have recommendations for this weather.")