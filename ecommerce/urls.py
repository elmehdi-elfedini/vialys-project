from django.contrib import admin
from django.urls import path, include
from products.views import acceuil
from django.conf import settings
from django.conf.urls.static import static
from products.views import page_404_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Custom 404 error handler
handler404 = page_404_view 
urlpatterns = [
    # Admin panel route
    path('vialys-admin/', admin.site.urls),    
    path('', acceuil, name='acceuil'),      
    path('products/', include('products.urls')),
    path('', include('blog.urls')), 
    path('ckeditor/', include('ckeditor_uploader.urls')),
] 

# Add media files (images, uploaded files) serving URLs
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Automatically serve static files during development (Django does this for you in debug mode)
urlpatterns += staticfiles_urlpatterns()
