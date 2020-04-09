from django.urls import path
from . import views


app_name = 'music'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:album_id>/favorite/', views.favorite, name='favorite'),
    path('album/add/', views.AlbumCreate.as_view(), name='album_add')
]