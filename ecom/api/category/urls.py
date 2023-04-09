from rest_framework import routers
from django.urls import path, include

from . import views
from .views import SearchView
router = routers.DefaultRouter()
router.register(r'', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/',SearchView.as_view(),name="search"),
]
