from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *


# Create your views here.
def index(request):
    all_album = Album.objects.all()
    html = ''
    for album in all_album:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)

def detail(request, album_id):
    return HttpResponse('<h2>Detail for album ID:' + str(album_id) + '</h2>')
