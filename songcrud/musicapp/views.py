from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import *


def artiste(request):
    artists = Artiste.objects.all()

    total_artists = artists.count()
    total_songs = Song.objects.all().count()
    total_lyrics = Lyric.objects.all().count()

    context = {'artists':artists,'total_artists': total_artists,
    'total_songs': total_songs, 'total_lyrics': total_lyrics}

    return render(request,'artiste.html',context)


def song(request,pk):
    songs = Song.objects.filter(artiste_id=pk)

    song_count = songs.count()

    context = {'songs':songs,'song_count':song_count}

    return render(request, 'song.html',context)


def lyric(request,pk,pk_1):
    songs = Song.objects.filter(artiste_id=pk)
    lyrics = songs.filter(Lyric.objects.get(artiste_id=pk, song_id=pk_1))

    context  = {'lyrics': lyrics}

    return render(request, context)
