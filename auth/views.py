from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from ninja import Form, Router
from django.core.validators import validate_email
from auth.jwt import create_token


api_auth = Router()


@api_auth.post('login/')
def login(request, username: str = Form(...), password: str = Form(...)):
    user = get_object_or_404(User, username=username)
    if check_password(password, user.password):
        return create_token(user.id)


@api_auth.post('register/')
def register(request, username: str = Form(...),
 password1: str = Form(...), password2: str = Form(...)):
    if password1 == password2:
        user = User.objects.create_user(username=username, password=password1)
        return f'User {user.username} criado com sucesso'
    return f'As senhas nao coincidem'
