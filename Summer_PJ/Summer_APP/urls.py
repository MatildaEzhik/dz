from django.urls import path
from . import views

urlpatterns = [
    path('', views.creation_story, name='creation_story'),
    path('characters/', views.characters, name='characters'),
    path('background_images/', views.background_images, name='background_images'),
    path('music_player/', views.music_player, name='music_player'),
]
