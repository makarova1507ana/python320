from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    # получить данные из БД
    # преобразовать / записать и т.д.
    return HttpResponse('Главная страница')
'''
Создайте маршрут 'news/' и представление, которое будет обрабатывать этот маршрут
Пусть на странице будет показано "Это страница новостей" 
'''

def news(request):
    return HttpResponse('Это страница новостей')




