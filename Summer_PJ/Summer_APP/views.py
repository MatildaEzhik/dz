from django.shortcuts import render

# Create your views here.
from .models import BackgroundImage, MusicTrack, Character


def music_player(request):
    tracks = MusicTrack.objects.all()
    context = {
        'tracks': tracks
    }
    return render(request, 'Summer_APP/music_player.html', context)

def creation_story(request):
    return render(request, 'Summer_APP/creation_story.html')

def characters(request):
    characters = Character.objects.all()
    context = {
        'characters': characters
    }
    return render(request, 'Summer_APP/characters.html', context)

def background_images(request):
    backgrounds = BackgroundImage.objects.all()
    context = {
        'backgrounds': backgrounds
    }
    return render(request, 'Summer_APP/background_images.html', context)
