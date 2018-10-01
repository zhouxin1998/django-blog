from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TypeInfo,BowenInfo

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','tTitle']

class BowenInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','bTitle','bPic','bDate','bClick','bComment','bIsDelete','bIstop']

admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(BowenInfo,BowenInfoAdmin)

