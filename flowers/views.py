from django.shortcuts import render
from .models import Flowers
import json
from django.http import JsonResponse




#queryset = YourModel.objects.filter(some__filter="some value").values()
#return JsonResponse({"models_to_return": list(queryset)})



def index(request):
    flowers = Flowers.objects.all().values()
    with open("base_flowers.json", "w") as write_file:
        json.dump(list(flowers), write_file)
    return render(request, 'index.html', {"flowers": flowers}
     ) 