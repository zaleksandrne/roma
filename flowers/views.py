
from django.shortcuts import render
from .models import Flowers




def index(request):
    flowers_list = Flowers.objects.all()
    return render(request, 'index.html', {"flowers_list": flowers_list}
     ) 