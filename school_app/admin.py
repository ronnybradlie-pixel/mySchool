from django.contrib import admin
from .models import School, Subscriber, Teacher

# Register your models here.
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'location', 'address', 'teachers')
    list_filter = ('location',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin): 
    list_display = ('name', 'subject', 'email')

    admin.site.register(Subscriber)