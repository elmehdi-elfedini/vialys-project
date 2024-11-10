# products/apps.py
from django.apps import AppConfig

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
    verbose_name = 'Gestion des Produits et de l\'Équipe'

    def ready(self):
        # Import ici pour éviter les imports circulaires
        from django.contrib.admin.apps import AdminConfig
        
        # Personnalisation de l'ordre des applications dans l'admin
        AdminConfig.default_site = 'django.contrib.admin.AdminSite'