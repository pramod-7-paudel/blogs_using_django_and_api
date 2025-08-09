from django.shortcuts import render
from django.http import JsonResponse
from .models import Blogbpost
from django.core.serializers import serialize
from django.utils import timezone
import json

def home(request):
    return render(request, 'task/post_list.html')

def get_posts(request):
    posts = Blogbpost.objects.all().order_by('-published_date')

    data = [
        {
            'title': post.title,
            'content': post.content,
            'author': post.author,
            'published': timezone.localtime(post.published_date).strftime('%Y-%m-%d %H:%M:%S')
                if post.published_date else "Unknown date",
        }
        for post in posts
    ]
    return JsonResponse(data, safe=False)