from django.contrib import admin
from .models import UserRegistrationModel

@admin.register(UserRegistrationModel)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'loginid', 'email', 'status')
    list_filter = ('status', 'city', 'state')
    search_fields = ('loginid', 'email', 'name')
