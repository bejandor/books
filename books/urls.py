"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from main.views import homepage,about, catalog
from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static # Импорт нужных библиотек

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',homepage, name='home'),
    path('index/',homepage, name='index'),
    path('about/',about, name='about'),
    path('catalog/',catalog, name='catalog'),
    path('add_,book/',add_book, name='add-book'),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
  # Прописали 2 строки кода которые нужны для корректной работы статичных фалов а
  # так же для медиа файлов