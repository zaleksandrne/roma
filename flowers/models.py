from django.db import models


class Flowers(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.TextField()
    image = models.ImageField(upload_to="/home/alex/code/roma/roma/flowers/static/image")
#/home/alex/code/roma/roma/flowers/static/image