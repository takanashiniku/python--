from django.contrib import admin
from .models import Department, Club, Employee

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Club)