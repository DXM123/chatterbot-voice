from chatterbot import ChatBot
from chatterbot.training.trainers import ChatterBotCorpusTrainer


bot = ChatBot(
    "Tiberius",
    io_adapters=[
        "chatterbot_voice.Voice"
    ]
)

bot.set_trainer(ChatterBotCorpusTrainer)

# Train the chat bot with the entire english corpus
bot.train("chatterbot.corpus.english")

user_input = ""

while True:
    try:
        user_input = bot.get_input()
        bot_input = bot.get_response(user_input)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
