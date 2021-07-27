from django.contrib import admin
from imageapp.models import ImageModel

@admin.register(ImageModel)
class ImageAdmin(admin.ModelAdmin):

    pass

# Register your models here.
