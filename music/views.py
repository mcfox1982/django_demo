from django.views import generic
from .models import *
from django.views.generic import CreateView,UpdateView,DeleteView


class IndexView(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
