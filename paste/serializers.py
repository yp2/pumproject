# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Paste


class PasteSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False,
                                  allow_blank=True,
                                  max_length=150)
    author = serializers.CharField(required=False,
                                   allow_blank=True,
                                   max_length=150)
    content = serializers.CharField(style={'type': 'textarea'})

    def create(self, validated_data):
        """
        Tworzy i zwraca instancje Paste
        :param validated_data:
        :return:
        """
        return Paste.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Modyfikuje i zwraca istniejaca instancje Paste
        :param instance:
        :param validated_data:
        :return:
        """
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
