from django.contrib import admin
from .models import Hyderabad
# Register your models here.


class HyderabadAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']


admin.site.register(Hyderabad,HyderabadAdmin)