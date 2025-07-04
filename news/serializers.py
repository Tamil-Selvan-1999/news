from rest_framework import serializers

from news.models import NewsModel, RoleModel, UserModel


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoleModel
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ["email", "password"]


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsModel
        fields = "__all__"
