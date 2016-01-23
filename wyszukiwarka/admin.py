from django.contrib import admin

# Register your models here.
from wyszukiwarka.models import *

admin.site.register(Marki)
admin.site.register(Samochody)
admin.site.register(Nadwozia)
admin.site.register(Silniki)
admin.site.register(Zdjecia)
admin.site.register(Silniki_Nadwozia)