def chatbot(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "what is your name":
        return "I'm a simple Python chatbot."

    elif user_input == "what can you do":
        return "I can chat with you using predefined replies."

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand that."


print("================================")
print("       BASIC CHATBOT")
print("================================")
print("Type 'bye' to exit the chatbot.\n")

while True:
    user_input = input("You: ")

    response = chatbot(user_input)
    print("Bot:", response)

    if user_input.lower() == "bye":
        break
print("\nChatbot session ended.")