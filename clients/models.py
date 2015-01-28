# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Client(models.Model):
    user = models.ForeignKey(
        User,
        related_name='client'
    )
    name = models.TextField(
        verbose_name=u"Nazwa"
    )
    address = models.TextField(
        verbose_name=u"Adres"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    modified = models.DateTimeField(
        auto_now=True
    )

    def __unicode__(self):
        return u'{} - ({})'.format(self.name, self.user.username)
