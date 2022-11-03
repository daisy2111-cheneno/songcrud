from django.forms import ModelForm
from .models import *

class ArtisteForm(ModelForm):
    class Meta:
        model = Artiste
        fields = '__all__'

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

class LyricForm(ModelForm):
    class Meta:
        model = Lyric
        fields = '__all__'
