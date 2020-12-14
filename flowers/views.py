from django.shortcuts import render
from .models import Flowers
import json
from pathlib import Path


def index(request):
    flowers = Flowers.objects.all().values()
    with open("/home/alex/code/roma/roma/flowers/static/base_flowers.json", "w") as write_file:
        json.dump(list(flowers), write_file, ensure_ascii=False)
    path = Path("/home/alex/code/roma/roma/flowers/static/base_flowers.json")
    data = json.loads(path.read_text())
    for i in range(0, len(data)):
        data[i]["image"] = data[i]["image"].replace("/home/alex/code/roma/roma/flowers", "")
    path.write_text(json.dumps(data, ensure_ascii=False))
    return render(request, 'index.html', {"flowers": flowers}) 



#/home/alex/code/roma/roma/flowers/static/base_flowers.json