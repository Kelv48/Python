# bot.py
#follows this tutorial https://realpython.com/build-a-chatbot-python-chatterbot/

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatbot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, friend 🤗",
])
trainer.train([
    "Are you a plant?",
    "No, I'm the pot below the plant!",
])

exit_conditions = (":q", "quit", "exit", "goodbye", "bye")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")