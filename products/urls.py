from django.urls import path
from .views import (
    acceuil,
    product_list,
    create_order,
    team_view,
    marque,
    contact,
    category_products  
)

urlpatterns = [
    path("", acceuil, name="acceuil"),
    path("products/", product_list, name="product-list"),
    path("marque/", marque, name="marque"),
    path("order/", create_order, name="order-create"),
    path("service_commercial/", team_view, name="service_commercial"),
    path("contact/", contact, name="contact"),
    path("category/<int:category_id>/", category_products, name="category-products"),  
]
