from django.shortcuts import render
from rest_framework.views import APIView
from .models import Accounts
from .serializers import registerSerializar
from rest_framework.response import Response
from rest_framework import status


class registerView(APIView):
    def post(self, request):
        if request.method == 'POST':
            serializer = registerSerializar(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_201_CREATED)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

