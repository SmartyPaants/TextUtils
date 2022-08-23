# I have created this file - Siddhant Kapoor
from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    return  render(request, 'index.html')

def analyse(request):                                       # Function name
    # Get the text
    text_web = request.GET.get('text', 'default')

    # Remove Punctuation
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~+=¬`|'''              # All punctuations
    removed_punc = ""
    for char in text_web:
        if char not in punctuation:
            removed_punc = removed_punc + char

    # UPPERCASE
    UPPERCASE = ""
    for char in text_web:
        UPPERCASE = UPPERCASE + char.upper()

    # lowercase
    lowercase = ""
    for char in text_web:
        lowercase = lowercase + char.lower()

    # Character Count (With Spaces)
    charcountwsp = len(text_web)

    # Character Count (Without Spaces)
    charcount = len(text_web)
    a = text_web.count(" ")
    charcountwisp = charcount - a

    # Word Count
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~+=¬`|'''              # All punctuations
    text = text_web.strip()
    count = 1
    for i in text:
        if i == " " or i == punctuations:
            count = count + 1
            wordcount = count
    
    # Sentence Count
    sentcount = ""
    a = text_web.count('.')
    b = text_web.count('?')
    c = text_web.count('!')
    x = a + b + c
    count1 = x
    sentcount = count1

    # Parameters
    params = {
        'wordcount': wordcount, 
        'sentcount': sentcount, 
        'og_text': text_web, 
        'remove_punc': removed_punc, 
        'UPPERCASE': UPPERCASE, 
        'lowercase': lowercase, 
        'charcountw': charcountwsp,
        'charcountwi': charcountwisp
    }

    # Sending information to 'analyse.html
    return render(request, 'analyse.html', params) 