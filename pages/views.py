from django.shortcuts import render


def HomePageView(request):
    return render(request, 'pages/index.html', {})


def AboutPageView(request):
    return render(request, 'pages/about.html', {})


def ContactPageView(request):
    if request.method == 'POST':
        print(request.method.POST['email'])
    return render(request, 'pages/contact.html', {})