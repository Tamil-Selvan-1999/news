from django.db import models

# Create your models here.


class RoleModel(models.Model):
    role = models.CharField(max_length=200)

    def __str__(self):
        return str(self.role)


class UserModel(models.Model):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    roles = models.ForeignKey(RoleModel, on_delete=models.CASCADE, related_name="users")

    def __str__(self):
        return str(self.username)


class NewsModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    category = models.CharField(max_length=200)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="news")

    def __str__(self):
        return str(self.title)
