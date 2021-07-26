from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post

# Create your views here.

#def index(request):
#    posts=Post.objects.all().order_by('-pk') #최신 글부터 올라오도록 하기 위해 작업
#
#    return render(
#        request,
#        'blog/index.html',
#        {
#            'posts' : posts,
#        }
#    )

#def single_post_page(request,pk):
#    post=Post.objects.get(pk=pk)
#    print(post)#
#
#    return render(
#        request,
#        'blog/single_post_page.html',
#        {
#            'post':post,
#        }
#    )