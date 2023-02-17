# prompt = "\nPlease, enter the name of a city you have visited:"
# prompt += "\nEnter 'quit' when you are finished. "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}")



prompt = "\nPlease enter access code:"
prompt += "\nEnter 'quit' for exit from this programm. "
while True:
    code = input(prompt)
    if code == 'quit':
        break
    else:
        print("Incorrect!")