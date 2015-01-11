# -*- coding: utf-8 -*-


from django.shortcuts import get_object_or_404
from .models import Paste
from .serializers import PasteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PasteList(APIView):
    """
    Lista wszystkich schowkow, lub utworzenie nowego
    """

    def get(self, request, author=None):
        if author:
            all_paste = Paste.objects.filter(author=author)
        else:
            all_paste = Paste.objects.all()

        serializer = PasteSerializer(all_paste, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PasteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasteDetail(APIView):
    """
    Pobierz, edytuj, usun schowek
    """

    def get(self, request, id):
        paste = get_object_or_404(Paste, id=id)
        serializer = PasteSerializer(paste)
        return Response(serializer.data)

    def put(self, request, id):
        paste = get_object_or_404(Paste, id=id)
        serializer = PasteSerializer(paste, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        paste = get_object_or_404(Paste, id=id)
        paste.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
