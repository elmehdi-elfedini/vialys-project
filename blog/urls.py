from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_list, name='blog_list'),  # Blog list page
    path('<int:id>/', views.blog_detail, name='blog_detail'),  # Blog detail page, with post id
]
