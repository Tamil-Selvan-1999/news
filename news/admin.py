from django.contrib import admin

from news.models import NewsModel, RoleModel, UserModel

# Register your models here.

admin.site.register(RoleModel)
admin.site.register(UserModel)
admin.site.register(NewsModel)
