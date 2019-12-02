from django.db import models

# Create your models here.
#from django.contrib.auth.models import Permission, User

from django.contrib.auth import get_user_model
User = get_user_model()

class Music(models.Model):
    GENRE_CHOICES = (
        ('P', 'Pop_Music'),
        ('E', 'Electronic_Dance_Music'),
        ('R', 'Rap_Music'),
        ('T', 'Trance_Music'),
        ('C', 'Classical_Music'),
        ('M', 'Mettal_Music'),
    )

    user = models.ForeignKey(User, related_name="user_music",on_delete=models.CASCADE)
    file = models.FileField(upload_to='music/')
    music_name = models.CharField(max_length=250)
    music_genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    music_logo = models.ImageField(upload_to='music/')
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.music_name + ' - ' + self.music_genre
