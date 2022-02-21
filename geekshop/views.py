from django.shortcuts import render


def index(request):
    title = 'Магазин'
    context = {
        'title': title,
    }
    return render(request, 'geekshop/index.html')

def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
    }
    return render(request, 'geekshop/contacts.html')
