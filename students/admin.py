from django.contrib import admin
from .models import Student,Nomenclature,Reason


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('surname','name','group','active','admission_date','notes')
    list_filter=('surname','name','group',)


@admin.register(Nomenclature)
class NomenclatureAdmin(admin.ModelAdmin):
    list_display=('title','unit')
    list_filter=('title','unit')

@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display=('name',)
   
