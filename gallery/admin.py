from django.contrib import admin
from .models import image,Category,tags, Location

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(image)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(tags)
