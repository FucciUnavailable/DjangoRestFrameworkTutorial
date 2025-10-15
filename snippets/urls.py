from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from snippets.models import Snippet
from snippets.views import api_root, SnippetViewSet, UserViewSet
from rest_framework.routers import DefaultRouter


# CREATE A ROUTER AND REGISTER VIEWSETS WITH IT
router = DefaultRouter()

router.register(r"snippets", views.SnippetViewSet, basename="snippet")
router.register(r"users", views.UserViewSet, basename="user")

# THE API URLS ARE NOT DETERMINED AUTOMATICALLY BY THE ROUTER
urlpatterns = {
    path("", include(router.urls)),
}
