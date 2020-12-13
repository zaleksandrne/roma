from django.db import models


class Flowers(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.TextField()
    image = models.ImageField(upload_to="/flowers/static/image", blank=True, null=True)
