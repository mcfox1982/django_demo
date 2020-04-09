from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
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
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'detail.html', {'album' : album })


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'detail.html', {'album':album, 'error_message': 'you selected nothing',})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'detail.html', {'album': album})