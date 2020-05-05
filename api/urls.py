# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'songs', views.SongView, basename='songs')
router.register(r'albums', views.AlbumViewSet,  basename='albums')
router.register('artists', views.ArtistViewSet, basename='artists')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),

]
