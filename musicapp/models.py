from tkinter import CASCADE
from django.db import models

# Create your models here.
  
class Artiste(models.Model):  
    first_name = models.CharField(max_length=200, null=True)  
    last_name = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Tag(models.Model):
    first_name = models.CharField(max_length=200, null=True)  
    last_name = models.CharField(max_length=200, null=True)
    

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste,null= True, blank= True, on_delete = models.SET_NULL)
    title = models.CharField(max_length = 200, null=True)
    date_released = models.DateField(auto_now_add = True, null=True)
    likes = models.IntegerField(null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title+ ' - ' + self.artiste_id.first_name + ' ' + self.artiste_id.last_name

class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)
    content = models.TextField(null = True, blank = True)
    

    def __str__(self):
        return self.song_id.title+ ' - ' + self.song_id.artiste_id.first_name + ' ' + self.song_id.artiste_id.last_name

