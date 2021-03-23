from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.security import HttpBearer
from .schemas import PostIn, PostOut
from .models import Post
from typing import List
from auth.jwt import AuthBearer


router_blog = Router()


@router_blog.post('/post')
def create_post(request, payload: PostIn):
    post = Post.objects.create(**payload.dict())
    return {'id': post.id}


@router_blog.get('/post/{post_id}', response=PostOut)
def get_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    return post


@router_blog.get('/posts', response=List[PostOut], auth=AuthBearer())
def list_posts(request):
    qs = Post.objects.all()
    return qs


@router_blog.put('/post/{post_id}')
def update_post(request, post_id: int, payload: PostIn):
    post = get_object_or_404(Post, id=post_id)
    for attr, value in payload.dict().items():
        setattr(post, attr, value)
    post.save()
    return {'success': True}


@router_blog.delete('/post/{post_id}')
def delete_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return {'success': True}
