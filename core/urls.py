from django.urls import path
from . import views
from .api import api


urlpatterns = [
    path('', views.api.urls),
]