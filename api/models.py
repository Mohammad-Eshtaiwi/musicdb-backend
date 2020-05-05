from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=60)
    bio = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=60)
    release_date = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.now().year)],
        help_text="Use the following format: <YYYY>"
    )
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name)


class Song(models.Model):
    name = models.CharField(max_length=60)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
