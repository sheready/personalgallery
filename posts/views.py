from django.shortcuts import render, get_object_or_404
from .models import *
import datetime as dt
from django.views.generic import ListView
from django.db.models import Q


def blog_view(request):
    posts = Post.objects.all()
    
    return render(request,'blog.html',{'posts':posts})

def detail_view(request, id):
    post = get_object_or_404(Post, id = id)
    photos = PostImage.objects.filter(post = post)

 
    return render(request,'detail.html',{
        'post':post,
        'photos':photos
    })


class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat':self.kwargs['category'],
            'posts':Post.objects.filter(category__name = self.kwargs['category'])
        }
        return content

def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list": category_list,

    }
    return context

