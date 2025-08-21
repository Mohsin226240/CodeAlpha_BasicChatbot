def simple_chatbot():
    """
    A simple rule-based chatbot that responds to predefined user inputs.
    The conversation continues until the user types 'bye' or 'quit'.
    """
    print("Chatbot: Hello! I'm a simple chatbot. How can I help you today?")
    print("Chatbot: You can say 'hello', 'how are you', or 'bye'.")

    while True:
        user_input = input("You: ").lower()
        if user_input in ["bye", "goodbye", "quit"]:
            print("Chatbot: Goodbye! Have a great day.")
            break
        elif user_input == "hello":
            print("Chatbot: Hi there! It's nice to chat with you.")
        elif user_input == "how are you":
            print("Chatbot: I'm just a program, but I'm doing great! Thanks for asking.")
        elif "name" in user_input:
            print("Chatbot: I don't have a name, but you can call me Bot.")
        elif "help" in user_input:
            print("Chatbot: I can answer basic questions like 'hello' or 'how are you'.")
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you rephrase?")
if __name__ == "__main__":
    simple_chatbot()
