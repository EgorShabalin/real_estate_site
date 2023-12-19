from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Heating)
admin.site.register(Photo)
admin.site.register(Parking)


class PhotoAdmin(admin.TabularInline):
    model = Photo


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin]

    class Meta:
        model = Property


admin.site.register(Property, PropertyAdmin)
