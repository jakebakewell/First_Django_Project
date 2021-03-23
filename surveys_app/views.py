from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

def register(request):
    return HttpResponse("placeholder for users to create a new user record")

def login(request):
    return HttpResponse("placeholder for users to log in")

def users_new(request):
    return redirect('/register')

def users(request):
    HttpResponse("placeholder to later display all the list of users")
