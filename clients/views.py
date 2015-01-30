# -*- coding: utf-8 -*-
from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from clients.models import Client
from clients.serializers import ClientSerializer
from rest_framework import status


class ClientList(APIView):

    def get(self, request, username=None):
        if username:
            all_clients = Client.objects.filter(user__username=username)
        else:
            all_clients = Client.objects.all()

        print all_clients

        serializer = ClientSerializer(all_clients, many=True)
        return Response(serializer.data)

    def post(self, requset):
        serializer = ClientSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientDetail(APIView):

    def get(self, request, username, remote_id):
        user = get_object_or_404(User, username=username)
        client = get_object_or_404(Client, remote_id=remote_id, user=user )
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, username, remote_id):
        user = get_object_or_404(User, username=username)
        client = get_object_or_404(Client, remote_id=remote_id, user=user )
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)