responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    vacation = input("Where do you want to rest in holidays? ")

    responses[name] = vacation

    repeat = input("would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("---Poll Results---")
for name, vacation in responses.items():
    print(f"{name} like rest in {vacation}")
