# responses = {}
#
# polling_active = True
#
# while polling_active:
#     name = input("\nWhat is our name? ")
#     response = input("Which mountain would you like to climb someday? ")
#
#     responses[name] = response
#
#     repeat = input("Would you like to let another person respon? (yes/no) ")
#     if repeat == 'no':
#         polling_active = False
#
# print("\n---Poll Result---")
# for name, response in responses.items():
#     print(f"{name} would like climb {response}.")


responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("What car is favourite for you? ")

    responses[name] = response

    repeat = input("whould you like to let another person respon? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("---Poll Results---")
for name, response in responses.items():
    print(f"{name.title()} like {response.title()}")