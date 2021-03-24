from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.security import HttpBearer
from .schemas import PostIn, PostOut
from .models import Post
from typing import List
from auth.jwt import AuthBearer, AuthBearerAdmin


router_blog = Router()


@router_blog.post('/post', auth=AuthBearer(), summary='Create a post')
def create_post(request, payload: PostIn):
    pay = dict(payload)
    post = Post.objects.create(owner=request.auth, title=pay['title'], content=pay['content'])
    return {'id': post.id}


@router_blog.get('/post/{post_id}', response=PostOut, summary='Get a post')
def get_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    return post


@router_blog.get('/posts/', response=List[PostOut], auth=AuthBearerAdmin(), summary='Get all posts *admin only*')
def list_posts(request):
    qs = Post.objects.all()
    return qs


@router_blog.put('/post/{post_id}', auth=AuthBearer(), summary='Update Post *Post owner only*')
def update_post(request, post_id: int, payload: PostIn):
    post = get_object_or_404(Post, id=post_id)
    if post.owner == request.auth:
        for attr, value in payload.dict().items():
            setattr(post, attr, value)
        post.save()
        return {'success': True}
    return f'Voce nao tem permissao para alterar este post!'


@router_blog.delete('/post/{post_id}', auth=AuthBearer(), summary='Delete a post')
def delete_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    if post.owner == request.auth:
        post.delete()
        return {'success': True}
    return f'Voce nao tem permissao para deletar este post'
