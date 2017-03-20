from django.contrib import admin
from invoice.models import Company, Project, Invoice

# Register your models here.

admin.site.register(Company)
admin.site.register(Project)
admin.site.register(Invoice)