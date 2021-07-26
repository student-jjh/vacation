from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    posts=Post.objects.all().order_by('-pk') #최신 글부터 올라오도록 하기 위해 작업

    return render(
        request,
        'blog/index.html',
        {
            'posts' : posts,
        }
    )