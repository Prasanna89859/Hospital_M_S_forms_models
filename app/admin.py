from django.contrib import admin
from app.models import *
# Register your models here.


class customizdepartment(admin.ModelAdmin):
    list_display=['name','slocation']
    search_fields=['name']
    list_filter=('name',)
admin.site.register(department,customizdepartment)

class customizDoctor(admin.ModelAdmin):
    list_display=['name','department']
    list_filter=('name',)
admin.site.register(Doctor,customizDoctor)

class customizpatient(admin.ModelAdmin):
    list_display=['name','tnumber','dob']
    list_filter=('name',)
    search_fields=['name']
admin.site.register(patient,customizpatient)

class customizeAM(admin.ModelAdmin):
    list_display=['Doctor','patient']
    list_filter=('patient',)
    search_fields=['patient']
admin.site.register(AM,customizeAM)

