from django.urls import path
from .views import Ready, Todo, CacheTest

urlpatterns = [
    path('', Todo.as_view(), name = "todo"),
    path('ready/', Ready.as_view(), name = "ready"),
    path('cache/', CacheTest.as_view(), name = "cache")
]
