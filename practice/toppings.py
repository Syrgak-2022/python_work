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


requested_toppings = []
if requested_toppings:
    for requested_toppings in requested_toppings:
        print(f"Adding {requested_toppings}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")