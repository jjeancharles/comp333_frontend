from tkinter import CASCADE
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator


# Create your models here.

class users (models.Model):
    username = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.username

    
class artists (models.Model):
    song = models.CharField(max_length=255, primary_key=True)
    artist = models.CharField(max_length= 255)
    def __str__(self):
        return self.song

class ratings (models.Model):
    username = models.ForeignKey(users, on_delete=models.CASCADE)
    song = models.ForeignKey(artists, on_delete=models.CASCADE) 
    rating = models.PositiveBigIntegerField(validators= [MinValueValidator(0), MaxValueValidator(5)])
    def __int__(self):
       return self.id

class songs (models.Model) :
    GENRE = (('Pop','Pop'), ('Hip-Hop','Hip-Hop'), ('Classic','Classic'), ('Rock','Rock'), ('Country','Country'))
    song = models.ForeignKey(artists, on_delete=models.CASCADE)#, primary_key=True)
    genre =  models.CharField(max_length=60,choices=GENRE)
    def __str__(self):
        return self.genre