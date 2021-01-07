from rest_framework import serializers
from .models import BehaviorLog


class BehaviorLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BehaviorLog
        fields = ('id', 'project_id', 'user_id', 'url', 'referer',
                  'dwell_time', 'click_count', 'refocus_count',
                  'created_at', 'updated_at')
