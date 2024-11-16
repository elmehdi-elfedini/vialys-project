from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import BlogPost
from django.db.models import Q

def blog_list(request):
    """
    This function handles the display of a list of blog posts, including pagination, search functionality,
    and recent posts.

    Parameters:
    request (HttpRequest): The request object containing information about the current HTTP request.

    Returns:
    HttpResponse: The rendered HTML template for the blog list page, containing the list of blog posts,
    recent posts, search query, and pagination information.
    """
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

def blog_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    recent_posts = BlogPost.objects.filter(published=True).order_by('-created_at')[:3] 
    return render(request, 'blog/blog_detail.html', {'post': post, 'recent_posts': recent_posts})
