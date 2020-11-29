from django.db import models


class Flowers(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.TextField()
