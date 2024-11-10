from django.contrib import admin
from django.urls import path, include
from products.views import acceuil 
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from products.views import page_404_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

handler404 = page_404_view # for 404 page
urlpatterns = [
    path('vialys-admin/', admin.site.urls),
    path('',acceuil, name='acceuil'),  
    path('', include('products.urls')),  
    path('', include('blog.urls')),  
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns+=staticfiles_urlpatterns()
