from django.contrib import admin
from .models import Store


class StoreAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Store._meta.fields]
    search_fields = ['name']
    list_filter = ['name', 'owner']
    list_editable = ['name', 'description', 'rating', 'owner']


admin.site.register(Store, StoreAdmin)
