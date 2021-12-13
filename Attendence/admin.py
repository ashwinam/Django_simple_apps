from django.contrib import admin
from .models import Student, models

# Register your models here.
# admin.site.register(Student)

@admin.register(Student)
class Student_info(admin.ModelAdmin):
    list_display = ['st_name','st_mail','st_class']