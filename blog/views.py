from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import BlogPost
from django.db.models import Q

def blog_list(request):
    posts = BlogPost.objects.filter(published=True).order_by('-created_at')
    query = request.GET.get('search')

    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(author__icontains=query))

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    recent_posts = BlogPost.objects.filter(published=True).order_by('-created_at')[:3]
    no_results = not posts.exists() and query 

    return render(request, 'blog/blog_list.html', {
        'posts': page_obj,
        'recent_posts': recent_posts,
        'no_results': no_results,  
        'query': query 
    })


def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog/blog_detail.html', {
        'post': post
    })


def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, published=True)    
    recent_posts = BlogPost.objects.filter(published=True).order_by('-created_at')[:3]    
    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'recent_posts': recent_posts
    })
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    recent_posts = BlogPost.objects.filter(published=True).order_by('-created_at')[:3] 
    return render(request, 'blog/blog_detail.html', {'post': post, 'recent_posts': recent_posts})
