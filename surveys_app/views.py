from django.shortcuts import render, HttpResponse, redirect


def surveys(request):
    return HttpResponse("placeholder to display all the surveys created")


def new_survey(request):
    return HttpResponse("placeholder for users to add a new survey")
