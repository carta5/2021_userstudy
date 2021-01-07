from django.db import models

# Create your models here.
class BehaviorLog(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    project_id = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    url = models.CharField(max_length=512, null=False)
    referer = models.CharField(max_length=512, null=True)
    dwell_time = models.IntegerField(default=0)
    click_count = models.IntegerField(default=0)
    refocus_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
