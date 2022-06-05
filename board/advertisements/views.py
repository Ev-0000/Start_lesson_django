from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'adventsements/index.html')

def cours(request):
    return render(request, 'adventsements/cours.html')

def shop(request):
    return render(request, 'adventsements/shop.html')

def newspaper(request):
    return render(request, 'adventsements/newspaper.html')

def works(request):
    return render(request, 'adventsements/works.html')