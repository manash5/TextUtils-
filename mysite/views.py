# I have created this file
from django.http import HttpResponse 
from django.shortcuts import render 
from django.urls import path 

def index(request):
    return render(request,'index.html')
    # return HttpResponse('''<h1>Homepage</h1>''')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    upper = request.POST.get('uppercase','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    print(removepunc)
    if removepunc == 'on':
        punctuations = '''!()-[]{};:\'"<>,./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char 
        params = {"purpose":"Remove Punctuation", "analyzed_text" : analyzed}
        djtext = analyzed

    if upper =='on':
        analyzed = djtext.upper()
        params = {"purpose":"Capitalize letters", "analyzed_text" : analyzed}
        djtext = analyzed

    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed 

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index-1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if (removepunc != "on" and upper != 'on' and newlineremover != 'on' and charcount != 'on' and extraspaceremover != 'on'):
        return HttpResponse('Please select an operator and try again')

    return render(request, 'analyze.html', params)
   