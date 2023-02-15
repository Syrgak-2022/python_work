# car = input("What car do you want to a buy? ")
# print(f"\nLet me see if I can find you a {car.title()}")


# order = input("How many seats do you want to book? ")
# if order >= '8':
#     print(f"Please wait!")
# else:
#     print(f"\nYour seats are ready!")


number = input("Enter your number: ")
number = int(number)
if number % 10 == 0:
    print("\nYour number is multiple!")
else:
    print("\nYour number is not multiple!")