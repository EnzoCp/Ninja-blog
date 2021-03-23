from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from core.views import router_blog
from auth.views import api_auth

api = NinjaAPI()

api.add_router('auth',api_auth)
api.add_router('blog',router_blog)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.urls),
]
