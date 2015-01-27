from django.contrib import admin

# Register your models here.
from paste.models import Paste


class PasteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Paste, PasteAdmin)