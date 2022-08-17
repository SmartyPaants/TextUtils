# I have created this file - Siddhant Kapoor
from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    return  render(request, 'index.html')

def analyse(request):
    # Get the text
    text_web = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~+=¬`|'''
        analysed = ""
        for char in text_web:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose': 'Removed Punctuations', 'analysed_text': analysed}
        return render(request, 'analyse.html', params)

    else:
        return HttpResponse('Error')