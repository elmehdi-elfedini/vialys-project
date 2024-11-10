# products/views.py
from .models import Product, Order
from django.http import HttpResponse
from .models import Product, Category, Brand
from django.shortcuts import render, redirect
from .models import Product, Order, Category, Brand,Tag
from django.contrib import messages
from django.db.models import Q
from .models import TeamMember


def acceuil(request):
    return render(request, 'products/acceuil.html')

def service_commercial(request):
    return render(request, 'products/service_commercial.html') 

def contact(request):
    return render(request, 'products/contact.html') 

def marque(request):
    categories = Category.objects.prefetch_related('brands').all() 
    return render(request, 'products/marque.html', {'categories': categories})


def product_list(request):
    search_query = request.GET.get('search', '')  
    selected_brand = request.GET.get('brand', '') 
    selected_tag = request.GET.get('tag', '')  
    selected_category = request.GET.get('category', '')  

    categories = Category.objects.prefetch_related('products__tags').all()
    category_products = {}
    products = Product.objects.all()

    if selected_brand:
        try:
            brand_obj = Brand.objects.get(pk=selected_brand)
            products = products.filter(brand=brand_obj)  
        except Brand.DoesNotExist:
            products = Product.objects.none()  

    if selected_tag:
        products = products.filter(tags__name__iexact=selected_tag)

    if selected_category:
        try:
            category_obj = Category.objects.get(pk=selected_category)
            products = products.filter(category=category_obj) 
            category_products[category_obj] = products.distinct() 
        except Category.DoesNotExist:
            products = Product.objects.none()  

    if search_query:
        products = products.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(emballage__icontains=search_query)
        ).distinct()  

    if not category_products:
        for category in categories:
            category_products[category] = products.filter(category=category).distinct()

    brands = Brand.objects.all()
    tags = Tag.objects.all()

    return render(request, 'products/product_list.html', {
        'category_products': category_products,
        'search_query': search_query,
        'selected_brand': selected_brand,
        'selected_tag': selected_tag,
        'selected_category': selected_category,  
        'categories': categories,
        'brands': brands, 
        'tags': tags, 
    })


def category_products(request, category_id):
    # Retrieve the category object for the given category_id
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        messages.error(request, 'Category not found.')
        return redirect('product-list')

    # Get the query parameters for search, brand, tag, and category
    search_query = request.GET.get('search', '')
    selected_brand = request.GET.get('brand', '')
    selected_tag = request.GET.get('tag', '')

    # Initialize the products to all products in the selected category
    products = Product.objects.filter(category=category)

    # Apply brand filter if selected
    if selected_brand:
        try:
            brand_obj = Brand.objects.get(pk=selected_brand)
            products = products.filter(brand=brand_obj)
        except Brand.DoesNotExist:
            products = Product.objects.none()  # No products if brand does not exist

    # Apply tag filter if selected
    if selected_tag:
        products = products.filter(tags__name__iexact=selected_tag)

    # Apply search filter if search query is present
    if search_query:
        products = products.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(emballage__icontains=search_query)
        ).distinct()

    # Get all categories, brands, and tags to show in the filters
    categories = Category.objects.all()
    brands = Brand.objects.all()
    tags = Tag.objects.all()

    # Render the product list with the selected filters and category information
    return render(request, 'products/product_list.html', {
        'category_products': {category: products.distinct()},
        'categories': categories,
        'brands': brands,
        'tags': tags,
        'search_query': search_query,
        'selected_brand': selected_brand,
        'selected_tag': selected_tag,
        'selected_category': category_id,  # The current selected category
        'current_category': category,  # Pass the current category object for display
    })

def create_order(request):
    if request.method == 'POST':
        order = Order(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            phone_number=request.POST.get('phone_number'),
            message=request.POST.get('message'),
            entreprise=request.POST.get('company'),
        )
        order.save()
        messages.success(request, 'Votre demande a été envoyée avec succès !')
        return redirect('product-list')

    messages.error(request, 'Invalid request method.')
    return redirect('product-list')


def team_view(request):
    team_members = TeamMember.objects.all().order_by('priority')
    print("Nombre de membres trouvés:", team_members.count())
    print("Membres:", [f"{member.name} - {member.role}" for member in team_members])
    
    context = {
        'team_members': team_members
    }
    return render(request, 'products/service_commercial.html', context)

def page_404_view(request, exception):
    return render(request, 'products/404.html', status=404)