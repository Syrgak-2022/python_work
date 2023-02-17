# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_toppings in requested_toppings:
#     print(f"Adding {requested_toppings}")
# print("\nFinished making you pizza!")



# Если в пиццерии закончится зеленый перец

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_toppings in requested_toppings:
#     if requested_toppings == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Adding {requested_toppings}.")
# print("\nFinished making your pizza!")


# requested_toppings = []
# if requested_toppings:
#     for requested_toppings in requested_toppings:
#         print(f"Adding {requested_toppings}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")



# available_topping = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# requested_topping = ['mushrooms', 'french fries', 'extra cheese']
# for requested_topping in requested_topping:
#     if requested_topping in available_topping:
#         print(f"Adding {requested_topping}.")
#     else:
#         print(f"Sorry, we don't have {requested_topping}.")
# print("\nFinished your making pizza!")


# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese']
#     }
# print(f"You ordered a {pizza['crust']} - crust pizza "
# "with the following toppings:")
# for topping in pizza['toppings']:
#     print("\t" + topping)


# prompt = "\nPlease, enter the toppings to your pizza:"
# prompt += "\nEnter 'quit' for exit. "
# while True:
#     toppings = input(prompt)
#     if toppings == 'quit':
#         break
#     else:
#         print(f"Your topping added to your order!")


# prompt = "\nPlease, choose parts to your order:"
# prompt += "\nEnter 'quit' for exit. "
# while True:
#     part = input(prompt)
#     if part == 'quit':
#         break
#     else:
#         print(f"Chosen part added to your order!")



# prompt = "\nPlease, choose the game for your library:"
# prompt += "\nEnter 'quit' for exit. "
# while True:
#     game = input(prompt)
#     if game == 'quit':
#         break
#     else:
#         print(f"Your game added to your library!")


# age = input("Please, how old are you? ")
# age = int(age)
# if age <= 3:
#     print("Your ticket is free!")
# if age > 3 and age <= 12:
#     print("Your ticket cost $10.")
# else:
#     print("Your ticket cost $15.")


# infinite cycle
# x = 1
# while x < 5:
#     print(x)


# prompt = "\nPlease, add your files:"
# prompt += "\nEnter 'quit' for exit. "
# active = True
# while active:
#     file = input(prompt)
#     if file == 'quit':
#         break
#     else:
#         print(f"Your file added!")



prompt = "\nPlease, choose your favourite heroes:"
prompt += "\nEnter 'quit' for exit from this programm. "
while True:
    heroes = input(prompt)
    if heroes == 'quit':
        break
    else:
        print(f"Your hero added to your favourite lists of heroes!")