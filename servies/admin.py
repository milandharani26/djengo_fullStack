from django.contrib import admin
from servies.models import Servies
# Register your models here.

class ServiesAdmin(admin.ModelAdmin):
    list_display=('servies_icon','servies_title','servies_des')

admin.site.register(Servies,ServiesAdmin)
