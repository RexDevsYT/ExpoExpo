import json
import re
import random_responses


# Load JSON data
def load_json(file):
    with open(file, 'r', encoding='utf-8') as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)


# Store JSON data
response_data = load_json("bot.json")


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        # Check if there are any required words
        for word in split_message:
            if word in required_words:
                required_score += 1

        # Check each word the user has typed
        for word in split_message:
            # If the word is in the response, add to the score
            if word in response["user_input"]:
                response_score += 1

        # Add a boost to the response score if there's any required word
        if required_score > 0:
            response_score += 10

        # Add score to list
        score_list.append(response_score)

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Check if input is empty
    if input_string == "":
        return "Por favor, escribe algo para que podamos conversar. 😊"

    # If there is no good response, return a random one.
    if best_response > 0:
        return response_data[response_index]["bot_response"]

    return random_responses.random_string()

def chat_loop():
    while True:
        user_input = input("You: ")
        print("Bot:", get_response(user_input))

# Verifica si main.py es el archivo principal que se está ejecutando
if __name__ == "__main__":
    chat_loop()
