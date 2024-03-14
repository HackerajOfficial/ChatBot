from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# bot = ChatBot('chatbot', read_only=False, logic_adaptors=['chatterbot.logic.BestMatch'])

# spacy.load('en_core_web_sm')

def chatbot(userMessage):
    chatbot = ChatBot('Hackeraj')

    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)

    # # Train the chatbot based on the english corpus
    # trainer.train("chatterbot.corpus.english")

    # # Train based on english greetings corpus
    # trainer.train("chatterbot.corpus.english.greetings")

    # # Train based on the english conversations corpus
    # trainer.train("chatterbot.corpus.english.conversations")

    # #Custom Train 
    # trainer = ListTrainer(chatbot)
    # trainer.train([
    # "How are you?",
    # "I am good.",
    # "That is good to hear.",
    # "Thank you",
    # "You're welcome."
    # ])

    response = chatbot.get_response(userMessage)
    return response

# Create your views here.

def blog(request):
    return render(request, template_name='blog.html')

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    print(userMessage)
    response = chatbot(userMessage)
    return HttpResponse(response)
