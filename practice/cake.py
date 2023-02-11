cake = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
print(f"You ordered a {cake['crust']} - crust cake "
      "with next toppings:")
for topping in cake['toppings']:
    print("\t" + topping)