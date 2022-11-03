from django.urls import path
from . import views 

urlpatterns = [    
    path('artists/', views.artiste_list, name='artists'),
    path('artists/<pk>/', views.artiste_detail, name='artist_id'),
    path('songs/', views.song_list, name='songs'),
    path('artists/<pk>/songs/<pk_1>/', views.song_detail, name='song_id'),
    path('lyrics/<pk_2>/', views.lyric_detail, name='lyrics'),
]