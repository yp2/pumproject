# -*- coding: utf-8 -*-
from django.contrib import admin
from clients.models import Client

# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client, ClientAdmin)