# I have created this file - Siddhant Kapoor

from django.http import HttpResponse


def index(request):
	return  HttpResponse("Hello")

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