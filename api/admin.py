from django.contrib import admin

# Register your models here.
from .models import BehaviorLog

class BehaviorLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_id', 'user_id', 'url', 'created_at', 'updated_at')

admin.site.register(BehaviorLog, BehaviorLogAdmin)
