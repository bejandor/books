from django.shortcuts import render,redirect
from .models import*

# Create your views here.

def homepage(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


# Эта функция нужна для того чтобы получить данные с базы в виде словаря
def catalog(request):
    books_data_list = Books_data.objects.all()
    return render(request, "catalog.html",{"books_data_list":books_data_list})    






def add_book(request):
    form_book = request.POST # Получаем словарь

    title = form_book['title'] # Записываем в переменные по ключу
    subtitle = form_book['subtitle']
    genre = form_book['genre']
    author = form_book['author']
    year = form_book['year']
    descriptiton = form_book['description']
    price = form_book['price']

    books_obj = Books_data(
        # Создаем обьект  и передаем значения полученые по ключам в атрибуты класса - 
        #  - нового объекта
        title = title,
        subtitle = subtitle,
        genre = genre,
        author = author,
        year_of_issue = year,
        describtion = descriptiton,
        price = price
    )
    books_obj.save() # Сохраняем в базе 
    return redirect(catalog) # Перенаправляем на страницу каталог