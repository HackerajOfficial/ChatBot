from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog(request):
    return render(request, template_name='blog.html')

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    print(userMessage)
    response = userMessage
    return HttpResponse(response)
