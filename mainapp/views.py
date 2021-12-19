from django.shortcuts import render

from mainapp.models import Product


def products(request):
    title = 'Каталог'
    products = Product.objects.all()[:5]

    links_menu = [
        {'href': 'products_all', 'name': 'Всё'},
        {'href': 'products_home', 'name': 'Дом'},
        {'href': 'products_office', 'name': 'Офис'},
        {'href': 'products_modern', 'name': 'Модерн'},
        {'href': 'products_classic', 'name': 'Классика'},
    ]
    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products,
    }
    return render(request, 'mainapp/products.html', context=context)
