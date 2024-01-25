from django.shortcuts import render

from django.http import HttpResponse

def home(request):

    peoples = [
        {'name' : 'Mayuri Giri', 'age' : 24},
        {'name' : 'Darshan Hirekurubar', 'age' : 23},
        {'name' : 'Anshul Sharma', 'age' : 22},
        {'name' : 'Harshit Hirekurubar', 'age' : 17},
    ]

    vegetables = ['Pumpkin', 'Tomato', 'Potato']

    return render(request, "home\index.html", context={'page': 'Django Tutorial', 'peoples' : peoples, 'vegetables' : vegetables})

def about(request):
    context = {'page' : 'About'}
    return render(request, "home/about.html", context)

def contact(request):
    context = {'page' : 'Contact'}
    return render(request, "home/contact.html", context)

def success_page(request):
    print("*" * 10)
    context = {'page' : 'Success Page'}
    return HttpResponse("<h1>Hey! This is a success page.</h1>")