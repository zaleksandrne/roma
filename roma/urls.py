from django.contrib import admin
from django.urls import include, path
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404, handler500

handler404 = "flowers.views.page_not_found"
handler500 = "flowers.views.server_error" 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("flowers.urls")),
    
]
