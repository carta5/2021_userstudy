from django.contrib import admin

from django.contrib import admin
from .models import Description
from .models import Task
from .models import TaskAnswer
from .models import PreQuestionnaireAnswer
from .models import PostQuestionnaireAnswer
from .models import ExitQuestionnaireAnswer
from .models import SearchResult


# # Register your models here.

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'infomation_1','infomation_2')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('pk','title','scenario')

class TaskAnswerAdmin(admin.ModelAdmin):
    list_display = (
                    'task',
                    'answer',
                    'created_at')

class PreQuestionnaireAnswerAdmin(admin.ModelAdmin):
    list_display = (
                    'knowledge',
                    'prior_belief',
                    'created_at')

class PostQuestionnaireAnswerAdmin(admin.ModelAdmin):
    list_display = (
                    'effort',
                    'created_at')


class ExitQuestionnaireAnswerAdmin(admin.ModelAdmin):
    list_display = (
                    'age',
                    'sex',
                    'education',
                    'created_at')

class SearchResultAdmin(admin.ModelAdmin):
    list_display = (
        'misc',
        'rank',
        'title',
        'url',
        'snippet',
    )

admin.site.register(Task, TaskAdmin)
admin.site.register(Description, DescriptionAdmin)
admin.site.register(TaskAnswer, TaskAnswerAdmin)
admin.site.register(PreQuestionnaireAnswer, PreQuestionnaireAnswerAdmin)
admin.site.register(PostQuestionnaireAnswer, PostQuestionnaireAnswerAdmin)
admin.site.register(ExitQuestionnaireAnswer, ExitQuestionnaireAnswerAdmin)
admin.site.register(SearchResult, SearchResultAdmin)