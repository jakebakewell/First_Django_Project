from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

def surveys(request):
    return HttpResponse(f"placeholder to display all the surveys created")

def new(request):
    return HttpResponse(f"placeholder for users to add a new survey")
