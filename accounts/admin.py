from django.contrib import admin
from .models import Student, Professor, SiteAdmin, Proctor

admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(SiteAdmin)
admin.site.register(Proctor)