from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request

app = Flask(__name__)

bot = 'Wangdu'
chatbot = ChatBot(botname,
    ## storage_adapter = 'chatterbot.storage.SQLStorageAdapter'
    logic_adapters = [
    {
        'import_path': 'chatterbot.logic.BestMatch',
        'default_response': 'I am sorry, but I do not understand.',
        'maximum_similarity_threshold': 0.8
    },
    {
        "import_path": "chatterbot.logic.MathematicalEvaluation"
    },
    {
        "import_path": "chatterbot.logic.UnitConversion"
    },

 ],
)

@app.route("/")
def home():
    return render_template('index.html')
