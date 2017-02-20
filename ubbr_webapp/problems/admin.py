from django.contrib import admin

# Register your models here.

from problems.models import ModelUbbr


class ModelUbbrAdmin(admin.ModelAdmin):
    class Meta:
        model = ModelUbbr
    list_display = ('__str__','description',)

admin.site.register(ModelUbbr,ModelUbbrAdmin)
