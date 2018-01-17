from django.contrib import admin


# Register your models here.

from .models import Task
class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
    ('General', {'fields': ['name','description','client']}),
    ('Dates', {'fields':['date_finished','date_expired']}),
    ('Flags', {'fields':['is_cancelled', 'is_complete','is_rejected']}),
    ]
admin.site.register(Task,TaskAdmin);
