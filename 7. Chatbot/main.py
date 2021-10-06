from flask import Flask, request, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

bot = ChatBot('bot', storage_adapter = 'chatterbot.storage.SQLStorageAdapter', database="botData.sqlite3")
#trainer = ChatterBotCorpusTrainer(bot)
#trainer.train("chatterbot.corpus.english")
#trainer.train("C:\\Users\\US\\Desktop\\Python Programming\\7. Chatbot\\data\\data.yaml")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')      # Get data from input, write JS to index.html
    a = "Bot: "
    b = str( bot.get_response(userText) )
    return  a+b

if __name__ == '__main__':
    app.run(debug = True)
    