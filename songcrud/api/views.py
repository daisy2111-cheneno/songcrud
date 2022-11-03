from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from musicapp.models import *
from .serializers import *


# Create your views here.
@api_view(['GET','POST'])
def artiste_list(request,format = None):

    if request.method == 'GET':
        artists = Artiste.objects.all()
        serializer = ArtisteSerializers(artists, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ArtisteSerializers(artists)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def artiste_detail(request,pk, format=None):

    try:
        artist = Artiste.objects.get(id=pk)
    except Artiste.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = ArtisteSerializers(artist)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArtisteSerializers(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)    
    elif request.method == 'DELETE':
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def song_list(request,format = None):

    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializers(songs, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SongSerializers(songs)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def song_detail(request,pk_1, format=None):

    try:
        song = Song.objects.get(id=pk_1)
    except Song.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = SongSerializers(song)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SongSerializers(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def lyric_list(request,format = None):

    if request.method == 'GET':
        lyrics = Lyric.objects.all()
        serializer = LyricSerializers(lyrics, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = LyricSerializers(lyrics)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def lyric_detail(request,pk_2, format=None):

    try:
        lyric = Lyric.objects.get(id=pk_2)
    except Lyric.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = LyricSerializers(lyric)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = LyricSerializers(lyric, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    elif request.method == 'DELETE':
        lyric.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
