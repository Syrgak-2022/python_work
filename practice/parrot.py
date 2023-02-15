prompt = "Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the programm. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)