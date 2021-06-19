from django.db import models

# Create your models here.

class Books_data(models.Model):
    title = models.CharField(max_length =  100)
    subtitle = models.CharField(max_length =  100)
    describtion = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits= 7 ,decimal_places = 2)
    genre = models.CharField(max_length = 40)
    author = models.CharField(max_length = 100)
    year_of_issue = models.DecimalField(max_digits = 4,decimal_places = 0)
    uploaded_at = models.DateField(auto_now_add = True)