from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *


# Create your views here.
def index(request):
    all_album = Album.objects.all()
    template = loader.get_template('index.html')
    context ={
        'all_album' : all_album ,
    }
    return render(request, 'index.html', context)

def detail(request, album_id):
    return HttpResponse('<h2>Detail for album ID:' + str(album_id) + '</h2>')
