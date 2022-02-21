from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


def products(request, pk=None):
    title = 'Каталог'
    products = Product.objects.all()[:5]

    links_menu = ProductCategory.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'Всё'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')


        context = {
            'title': title,
            'links_menu': links_menu,
            'products': products,
            'category': category,
            'basket': basket,
        }
        return render(request, 'mainapp/products.html', context=context)

    same_products = Product.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': same_products,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', context=context)
