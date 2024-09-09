import random

responses = {
    "hello": ["Hi!", "Hello!", "Hey!"],
    "how are you": ["I'm good, thanks!", "I'm doing well. How about you?"],
    "default": ["I'm not sure how to respond to that.", "Can you please rephrase that?"],
}

def get_response(message):
    message = message.lower()
    for key in responses:
        if key in message:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Example usage:
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = get_response(user_input)
    print(f"Bot: {response}")
