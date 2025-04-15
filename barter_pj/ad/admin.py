from django.contrib import admin

from ad.models import Ad, Category, AdCategory

admin.site.register(Ad)
admin.site.register(Category)
admin.site.register(AdCategory)