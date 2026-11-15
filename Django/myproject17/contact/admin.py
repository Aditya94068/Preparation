from django.contrib import admin
from contact.models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','message','created')











# from django.contrib import admin
# from students.models import Student

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('name','age','city')
#     search_fields = ('name','city')
#     list_filter = ('age','city')
#     ordering = ('name',)