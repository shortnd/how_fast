from django.shortcuts import render

from . import forms

def HomePageView(request):
    return render(request, 'pages/index.html', {})


def AboutPageView(request):
    return render(request, 'pages/about.html', {})


def ContactPageView(request):
    context = {}
    if request.method == 'POST':
        context = {
            'email': request.POST['email']
        }
    return render(request, 'pages/contact.html', context)