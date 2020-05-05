from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SongSerializer, AlbumSerializer, ArtistSerializer
from .models import Song, Artist, Album
# Create your views here.


class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
