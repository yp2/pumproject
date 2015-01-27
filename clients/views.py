# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from clients.models import Client
from clients.serializers import ClientSerializer
from rest_framework import status


class ClientList(APIView):

    def get(self, request, user=None):
        if user:
            pass
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

    def get(self, request, id):
        client = get_object_or_404(Client, id=id)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, id):
        client = get_object_or_404(Client, id=id)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)