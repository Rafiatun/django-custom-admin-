from django.contrib import admin
from django.contrib.auth.models import Group
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import path
from django.utils.html import format_html
# Register your models here.

class snippetadmin(admin.ModelAdmin):
    list_display=('title','date_created','font_size_display')
    list_filter=('date_created',)
    change_list_template='admin.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls=[
            path('Fontsize/<int:size>/',self.change_font_size)
        ]

        return custom_urls + urls

    def change_font_size(self,request,size):
        self.model.objects.all().update(font_size=size)
        self.message_user(request,'Font size changed successfully')
        return HttpResponseRedirect("../")

    def font_size_display(self,obj):
        display_size=obj.font_size if obj.font_size <= 30 else 30
        return format_html(
            f'<span style="font-size: {display_size}px;">{obj.font_size}</span>'
        )

admin.site.site_header='Cutomized Admin Panel Making'
admin.site.register(snippet,snippetadmin)
admin.site.unregister(Group)