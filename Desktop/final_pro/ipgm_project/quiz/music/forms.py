from django import forms
from .models import Music


class MusicForm(forms.ModelForm):

    class Meta:
        model = Music
        fields = [
            'music_name',
            'music_genre',
            'music_logo',
            'file'
        ]
