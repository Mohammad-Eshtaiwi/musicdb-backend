import graphene
from graphene_django import DjangoObjectType
from .models import *


class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album


class SongType(DjangoObjectType):
    class Meta:
        model = Song


class Query(object):
    all_artists = graphene.List(ArtistType)

    artist = graphene.Field(ArtistType,
                            id=graphene.Int(),
                            name=graphene.String())

    all_albums = graphene.List(AlbumType)

    album = graphene.Field(AlbumType,
                           id=graphene.Int(),
                           name=graphene.String())

    all_songs = graphene.List(SongType)

    song = graphene.Field(SongType,
                          id=graphene.Int(),
                          name=graphene.String())

    def resolve_all_artists(self, info, **kwargs):
        return Artist.objects.all()

    def resolve_all_albums(self, info, **kwargs):
        return Album.objects.select_related('artist').all()

    def resolve_all_songs(self, info, **kwargs):
        return Song.objects.select_related('album').all()

    def resolve_artist(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Artist.objects.get(pk=id)

        if name is not None:
            return Artist.objects.get(name=name)

        return None

    def resolve_album(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Album.objects.get(pk=id)

        if name is not None:
            return Album.objects.get(name=name)

        return None

    def resolve_song(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Song.objects.get(pk=id)

        if name is not None:
            return Song.objects.get(name=name)

        return None
