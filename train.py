import sys
from chatbot import bot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
time.clock = time.time

print(sys.prefix)
print("train")

trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    "chatterbot.corpus.english"
)

trainer.train([
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
])

print("endchattrain")