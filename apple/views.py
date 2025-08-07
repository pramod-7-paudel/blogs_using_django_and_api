from django.shortcuts import render
from django.http import JsonResponse
from .models import Blogbpost
from django.core.serializers import serialize
import json

def home(request):
    return render(request, 'task/post_list.html')

def get_posts(request):
    posts = Blogbpost.objects.all().order_by('-published')
    data = [
        {'title': post.title,
            'content': post.content,
            'published': post.published.strftime('%Y-%m-%d %H:%M:%S'),
        } for post in posts 
    ]
    return JsonResponse(data, safe=False)