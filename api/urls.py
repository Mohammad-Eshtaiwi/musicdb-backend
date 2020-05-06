# myapi/urls.py
from django.urls import include, path
from . import views

from graphene_django.views import GraphQLView

urlpatterns = [
    path("graphql", GraphQLView.as_view(graphiql=True)),
]
