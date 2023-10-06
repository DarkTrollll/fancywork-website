from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def examples(request):
    return render(request, "examples.html")


def contact(request):
    return render(request, "contact.html")

