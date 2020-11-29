from django.contrib import admin
from .models import Flowers





class FlowersAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price",) 
    search_fields = ("name",) 
    list_filter = ("price",) 
    empty_value_display = "-пусто-"
 
admin.site.register(Flowers, FlowersAdmin)
