    
from django.urls import path
from . import views 

urlpatterns = [    
    path('artists/', views.artiste_list, name='artists'),
    path('artists/<pk>/', views.artiste_detail, name='artist_id'),
    path('songs/', views.song_list, name='songs'),
    path('songs/<pk_1>/', views.song_detail, name='song_id'),
    path('lyrics/', views.lyric_list, name='lyrics'),
    path('lyrics/<pk_2>/', views.lyric_detail, name='lyric_id'),
#     path('song/<pk>/lyric/<pk_1>/', views.lyric, name='lyrics'),

#     path('add_artiste/', views.addArtiste, name='add_artiste'),
#     path('update_artiste/<pk>/', views.updateArtiste, name='update_artiste'),
#     path('delete_artiste/<pk>/', views.deleteArtiste, name='delete_artiste'),

    
#     path('add_song/', views.addSong, name='add_song'),
#     path('song/<pk>/update_song/<pk_1>/', views.updateSong, name='update_song'),
#     path('song/<pk>/delete_song/<pk_1>/', views.deleteSong, name='delete_song'),

#     path('add_lyrics/', views.addSong, name='add_lyrics'),
]