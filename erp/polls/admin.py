# from django.contrib import admin

# # Register your models here.
from django.contrib import admin

from .models import student,department,faculty,course,enrollment
admin.site.site_header = 'ERP Administration'
admin.site.site_title = 'ERP site Admin'
admin.site.register(student)
admin.site.register(department)
admin.site.register(faculty)
admin.site.register(course)
admin.site.register(enrollment)

