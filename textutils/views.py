# I have created this file - Siddhant Kapoor
from django.http import HttpResponse
from django.shortcuts import render 


def index(request):
    info = {'name':'Siddhant & Soubhagya', 'place':'Unknown Galaxy'}
    return  render(request, 'index.html', info)


def removepunc(request):
    return  HttpResponse("Remove Puctuation")


def capfirst(request):
    return  HttpResponse("Capitalise First")


def newlineremove(request):
    return  HttpResponse("New Line Remover")


def spaceremove(request):
    return  HttpResponse("Space Remover")


def charcount(request):
    return  HttpResponse("Character Count")