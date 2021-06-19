from django.contrib import admin
from .models import Books_data


# Для того чтобы наши поля(конструктор) появились в админ панели
# И по этому шаблону будет созданы обьекты и будут храниться в базе как целостные обьекты со 
# со своими методами

admin.site.register(Books_data)