from django.contrib import admin
from .models import Todo, Profile, TodaysNotes, TestUser

class ProfileAdmin(admin.ModelAdmin):
   list_display = ('user', 'google_token')
   
class TodoAdmin(admin.ModelAdmin):
   list_display = ('user', 'message', 'created_at' )
   
class TestUserAdmin(admin.ModelAdmin):
   list_display = ('name', 'email', )
   
admin.site.register(Profile)
admin.site.register(Todo)
admin.site.register(TodaysNotes)
admin.site.register(TestUser,TestUserAdmin)