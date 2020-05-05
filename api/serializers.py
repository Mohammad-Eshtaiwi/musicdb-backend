from .models import Song, Artist, Album
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    artist = serializers.CharField(read_only=True, source="album.artist.name")
    album = serializers.CharField(read_only=True, source="album.name")
    print('hello')
    print(artist.source)

    class Meta:
        model = Song
        fields = ('id', 'name', 'album', 'artist')
        print(fields)


class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.CharField(read_only=True, source="artist.name")

    class Meta:
        model = Album
        fields = ("id", "name", "release_date", 'artist')


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("id", "name", "bio")
