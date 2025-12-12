from django.contrib import admin

from home.models import TestModel

# Register your models here.

admin.site.register(TestModel)

class TestModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')