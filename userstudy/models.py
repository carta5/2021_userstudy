from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#タスクの事前情報 
class Description(models.Model):
    #1:ネガティブ 2:バイアスなし 3:ポジティブ
    infomation_1 = models.TextField()
    infomation_2 = models.TextField()
    infomation_3 = models.TextField()
   

class Task(models.Model):
    title = models.CharField(max_length=255)
    scenario = models.TextField(null=True, blank=True)
    search_url = models.CharField(max_length=255)
    pre_infomation = models.ForeignKey(Description, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PreQuestionnaireAnswer(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    knowledge = models.IntegerField(default=0)
    prior_belief = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#動画の内容をまとめる
class VideoContentCheck(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    video_content = models.TextField()

class TaskAnswer(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    answer = models.IntegerField(default=0)
    reason = models.TextField()
    url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostQuestionnaireAnswer(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    effort = models.IntegerField(default=0)
    evidence_existence = models.IntegerField(default=0)
    freshness = models.IntegerField(default=0)
    comprehensibility = models.IntegerField(default=0)
    source_expertise = models.IntegerField(default=0)
    aesthetics = models.IntegerField(default=0)
    content_coverage = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ExitQuestionnaireAnswer(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    e_health_literacy_q1 = models.IntegerField(default=0)
    e_health_literacy_q2 = models.IntegerField(default=0)
    e_health_literacy_q3 = models.IntegerField(default=0)
    e_health_literacy_q4 = models.IntegerField(default=0)
    e_health_literacy_q5 = models.IntegerField(default=0)
    e_health_literacy_q6 = models.IntegerField(default=0)
    e_health_literacy_q7 = models.IntegerField(default=0)
    e_health_literacy_q8 = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    sex = models.IntegerField(default=0)
    education = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SearchResult(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=512)
    snippet = models.CharField(max_length=512)
    rank = models.IntegerField(default=1)
    misc = models.CharField(max_length=255)
    #0:No 1:Yes
    is_public_institute = models.IntegerField(default=0)
  
