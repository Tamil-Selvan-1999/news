# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from news.models import NewsModel
from news.serializers import NewsSerializer, UserSerializer

# Create your views here.


class RegisterView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        if data:
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"msg": "Data Incomplete"}, status=status.HTTP_400_BAD_REQUEST)


class ListNewsView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, _request):
        news = NewsModel.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
