from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# Create your views here.

def index(request):
    # получить данные из БД
    # преобразовать / записать и т.д.
    # return HttpResponse('Главная страница')
    return render(request, "index.html")

'''
Создайте маршрут 'news/' и представление, которое будет обрабатывать этот маршрут
Пусть на странице будет показано "Это страница новостей" 
'''
def catalog(request):
    products = Product.objects.all()
    data = {'products': products}
    return render(request, 'catalog.html', data)

def product(request, product_id):
    data = {'product': Product.objects.get(id=product_id)}
    return render(request, 'product.html', data)

def news(request):
    return HttpResponse('Это страница новостей')



#---------------------работа с моделями---------------------------#
'''
CRUD - CREATE READ UPDATE DELETE

# Создать товар
product = Product(name='Товар1', price=1000.0, stock = 100)
product.save()


product = Product(name='Товар2', price=1250.50, stock = 78)
product.save()

# Получить все записи в  таблице товаров
products = Product.objects.all()

# получить о конкретном товаре
products.get(id=1)
Product.objects.get(id=1)
Product.objects.filter(name='Товар2')

product = Product(name='Товар2', price=100, stock = 7)
product.save()


# Изменить информаию о товаре
product_edit = Product.objects.get(id=3)
product_edit.name='Товар3'
product_edit.save()

Product.objects.get(id=3)

'''
