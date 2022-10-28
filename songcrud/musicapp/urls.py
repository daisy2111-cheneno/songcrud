    
from django.urls import path, re_path
from . import views 

urlpatterns = [    
    path('', views.artiste, name='artists'),
    path('song/<pk>/', views.song, name='songs'),
    path('song/<pk>/lyric/<pk_1>/', views.lyric, name='lyrics'),
]