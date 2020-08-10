from django.contrib import admin

from .models import Topics, Groups

class TopicsAdmin(admin.ModelAdmin):
	list_display = ["name"]

class GroupsAdmin(admin.ModelAdmin):
	list_display = ["name", "topic"]  

admin.site.register(Topics, TopicsAdmin)
admin.site.register(Groups, GroupsAdmin)