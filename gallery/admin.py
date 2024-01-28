from django.contrib import admin
from .models import Image, Review, Category

# Register models
admin.site.register(Image)
admin.site.register(Review)
admin.site.register(Category)

