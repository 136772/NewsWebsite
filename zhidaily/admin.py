from django.contrib import admin
from zhidaily.models import *

# Register your models here.
# 库中超级用户名密码: Admin/Admin123456


@admin.register(Best)
class BestAdmin(admin.ModelAdmin):
    list_display = ('select_article','sort',)
    list_editable = ('sort',)


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name','display')
    list_editable = ('display',)


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Comment)
