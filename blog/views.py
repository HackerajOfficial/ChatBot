from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# bot = ChatBot('chatbot', read_only=False, logic_adaptors=['chatterbot.logic.BestMatch'])

import re
import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")


from .models import UserInfo

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

    #call extract information
    name, email, address, phone_number = extract_info(userMessage)
    print("Name:", name)
    print("Email:", email)
    print("Address:", address)
    print("Phone number:", phone_number)

    # Create a UserInfo object and save it to the database
    user_info = UserInfo.objects.create(name=name, email=email, mobile_number=phone_number, address=address)


    response = chatbot(userMessage)
    return HttpResponse(response)

def extract_info(message):
    # Initialize variables to store extracted information
    name = None
    email = None
    address = None
    phone_number = None
    
    # Regular expressions for email and phone number
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # phone_pattern = r'\b(?:\d{3}[-.]|\(\d{3}\) ?)\d{3}[-.]\d{4}\b'
    phone_pattern = r'(?:(?:\+?\d{1,3}[\s.-]?)?(?:\(\d{1,3}\)[\s.-]?)?)?\d{3,4}[\s.-]?\d{3,4}[\s.-]?\d{3,4}'

    
    # Regex search for email and phone number
    email_match = re.search(email_pattern, message)
    phone_match = re.search(phone_pattern, message)
    
    if email_match:
        email = email_match.group(0)
        
    if phone_match:
        phone_number = phone_match.group(0)

    #Look for keywords indicating an address
    # address_keywords = ['street', 'road', 'avenue', 'city', 'town', 'zip code','live at']
    # for keyword in address_keywords:
    #     if keyword in message.lower():
    #         address_match = re.search(r'\b\d+\s+\w+\s+\w+,\s+\w+\b', message)
    #         if address_match:
    #             address = address_match.group(0)
    #             break

    # Perform named entity recognition for extracting name, and address
    doc = nlp(message)
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            name = ent.text
        elif ent.label_ == 'GPE':  # Check for geopolitical entities (e.g., locations)
            address = ent.text
        elif ent.label_ == 'LOC':  # Check for general locations
            address = ent.text
        elif ent.label_ == 'FAC':  # Check for facilities
            address = ent.text
    
    return name, email, address, phone_number


