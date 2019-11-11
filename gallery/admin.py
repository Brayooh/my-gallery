from django.contrib import admin
from .models import image,Category,tags, Location

class imageAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(image, imageAdmin)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(tags)
