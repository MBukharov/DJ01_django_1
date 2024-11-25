from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Готовые страницы:</h1>"
                        "<p>Страница <a href='/test'>test</a></p><br>"
                        "<p>Страница <a href='/data'>data</a></p>")

def data(request):
    return HttpResponse("<h1>Данные:</h1>")

def test(request):
    return HttpResponse("<h1>Тест:</h1>")