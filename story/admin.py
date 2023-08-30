from django.contrib import admin

# Register your models here.
from .models import Books, Comments, Audio

admin.site.register(Books)
admin.site.register(Comments)
admin.site.register(Audio)