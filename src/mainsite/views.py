from django.shortcuts import render
from .models import MyBow

# Create your views here.


def home(request):
    return render(request, 'mainsite/index.html')


def aboutme(request):
    return render(request, 'mainsite/aboutme.html')


def wood(request):
    return render(request, 'mainsite/wood.html')


def gallery(request):
    bows = MyBow.objects.all()
    return render(request, 'mainsite/gallery.html', {'bows': bows})


def contact(request):
    return render(request, 'mainsite/contact.html')
