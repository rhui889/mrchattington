import sys
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
time.clock = time.time

print(sys.prefix)
print("Hello, World!")


bot  = ChatBot('test',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
     logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'
    )


from chatterbot.trainers import ChatterBotCorpusTrainer
print("train")
trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    "chatterbot.corpus.english"
)

from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train([
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])
print("chattington")

while True:
    try:
        bot_input = bot.get_response(input())
        print("bot: ")
        print(bot_input)
        print("endbot ")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break

print("Exit app")