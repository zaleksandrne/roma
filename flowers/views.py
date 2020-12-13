from django.shortcuts import render
from .models import Flowers
import json


def index(request):
    flowers = Flowers.objects.all().values()
    with open("/home/alex/code/roma/roma/flowers/static/base_flowers.json", "w") as write_file:
        json.dump(list(flowers), write_file, ensure_ascii=False)
    return render(request, 'index.html', {"flowers": flowers}) 



#/home/alex/code/roma/roma/flowers/static/base_flowers.json