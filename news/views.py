# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import AccessToken

from news.models import NewsModel, UserModel
from news.serializers import NewsSerializer

# Create your views here.


class LoginView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        if email is not None and password is not None:
            try:
                user = UserModel.objects.get(email=email)
            except UserModel.DoesNotExist:
                return Response(
                    {"msg": "Incorrect credentials"}, status=status.HTTP_400_BAD_REQUEST
                )
            if password == user.password:
                return Response(
                    {
                        "username": user.username,
                        "token": str(AccessToken.for_user(user)),
                    },
                    status=status.HTTP_200_OK,
                )
        return Response(
            {"msg": "Incomplete request"}, status=status.HTTP_400_BAD_REQUEST
        )


class ListNewsView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, _request):
        news = NewsModel.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
