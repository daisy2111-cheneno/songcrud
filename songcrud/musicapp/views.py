from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *
from .forms import *
from api.views import *



# def artiste(request):
#     artists = Artiste.objects.all()

#     total_artists = artists.count()
#     total_songs = Song.objects.all().count()
#     total_lyrics = Lyric.objects.all().count()

#     context = {'artists':artists,'total_artists': total_artists,
#     'total_songs': total_songs, 'total_lyrics': total_lyrics}

#     return render(request,'artiste.html',context)


# # def song(request,pk):
#     artist = Artiste.objects.get(id=pk)
#     songs = Song.objects.filter(artiste_id=pk)

#     song_count = songs.count()

#     context = {'artist': artist,'songs':songs,'song_count':song_count}

#     return render(request, 'song.html',context)


# def lyric(request,pk,pk_1):
#     songs = Song.objects.filter(artiste_id=pk)
#     lyric = Lyric.objects.get(song_id=pk_1)

#     context  = {'songs': songs, 'lyric': lyric}

#     return render(request, 'lyric.html', context)


# def addArtiste(request):
    
#     form = ArtisteForm()
#     if request.method == 'POST':
#         # print('Printing POST:',request.POST)
#         form = ArtisteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

    
#     context ={'form':form}
#     return render(request, 'views_form.html', context)

# def updateArtiste(request,pk):
#     artist = Artiste.objects.get(id=pk)
#     form = ArtisteForm(instance=artist)

#     if request.method == 'POST':
#         # print('Printing POST:',request.POST)
#         form = ArtisteForm(request.POST, instance=artist)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     context = {'form':form}

#     return render(request, 'views_form.html', context)
    
# def deleteArtiste(request,pk):
#     artist = Artiste.objects.get(id=pk)

#     if request.method == 'POST':
#         artist.delete()
#         return redirect('/')

#     context={'artist': artist}
#     return render(request,'delete_artiste.html', context)


# def addSong(request):
#     form = SongForm()
#     if request.method == 'POST':
#         # print('Printing POST:',request.POST)
#         form = SongForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

    
#     context ={'form':form}

#     return render(request, 'views_form.html', context)


# def updateSong(request,pk,pk_1):
#     song = Song.objects.get(artiste_id=pk)
#     lyric = Lyric.objects.get(song_id = pk_1)

#     form = SongForm(instance=song)

#     if request.method == 'POST':
#         # print('Printing POST:',request.POST)
#         form = SongForm(request.POST, instance=song)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     context = {'form':form}

#     return render(request, 'views_form.html', context)
    
# def deleteSong(request,pk,pk_1):
#     song = Song.objects.get(artiste_id=pk)
#     lyric = Lyric.objects.get(song_id=pk_1)

#     if request.method == 'POST':
#         song.delete()
#         return redirect('song/')

#     context={'song': song, 'lyric': lyric}
#     return render(request,'delete_song.html', context)


# def addLyric(request):
    # form = LyricForm()
    # if request.method == 'POST':
    #     # print('Printing POST:',request.POST)
    #     form = LyricForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')

    
    # context ={'form':form}

    # return render(request, 'views_form.html', context)






