# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.Serializer):

    pk = serializers.IntegerField(read_only=True)
    user = serializers.CharField()
    remote_id = serializers.IntegerField()
    name = serializers.CharField()
    address = serializers.CharField(required=False)

    def create(self, validated_data):
        user = validated_data.get('user')
        user = get_object_or_404(User, username=user)
        validated_data['user'] = user
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user = validated_data.get('user', None)
        if user:
            user = get_object_or_404(User, username=user)
            validated_data['user'] = user
            instance.user = validated_data.get('user')
        else:
            instance.user = instance.user
        instance.remote_id = validated_data.get('remote_id', instance.remote_id)
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance



