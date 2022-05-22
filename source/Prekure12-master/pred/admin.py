from django.contrib import admin
from .models import Report,Doctor,Post,Replie
# Register your models here.

admin.site.register(Report)

admin.site.register(Post)
admin.site.register(Replie)


class DoctorAdmin(admin.ModelAdmin):
    list_display=["name","age","experience","area","state","address","phone_number","fees","img"]


admin.site.register(Doctor,DoctorAdmin)