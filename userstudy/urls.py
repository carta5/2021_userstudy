from django.urls import path
from . import views
from .views import IndexView
from .views import StartView
from .views import ReadyView
from .views import PreQuestionnaireView
from .views import TaskIntroductionFirstView
from .views import TaskIntroductionSecondView
from .views import TaskIntroductionThirdView 
from .views import TaskIntroductionFourthView 
from .views import SearchResultListView
from .views import PostQuestionnaireView
from .views import ExitQuestionnaireAnswerView
from .views import WorkCompletionView

from .views import show_archived_html

#add
from .views import VideoContentCheckView

app_name = 'userstudy'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('start',StartView.as_view(),name='start'),
    path('ready', ReadyView.as_view(), name='ready'),
    path('pre-questionnaire',
          PreQuestionnaireView.as_view(), name='pre_questionnaire'),
    path('task_introduction_1',
         TaskIntroductionFirstView.as_view(), name='task_introduction_1'),
    path('task_introduction_2',
        TaskIntroductionSecondView.as_view(), name='task_introduction_2'),
    path('task_introduction_3',
        TaskIntroductionThirdView.as_view(), name='task_introduction_3'),
    path('task_introduction_4',
        TaskIntroductionFourthView.as_view(), name='task_introduction_4'),
    path('video_content_check',
        VideoContentCheckView.as_view(), name='video_content_check'),
    path('search',
         SearchResultListView.as_view(), name='search'),
    path('post-questionnaire',
         PostQuestionnaireView.as_view(), name='post_questionnaire'),
    path('exit-questionnaire',
        ExitQuestionnaireAnswerView.as_view(), name='exit_questionnaire'),
    path('complete', WorkCompletionView.as_view(), name='complete'),
    path('archive/<int:page_id>/',
         show_archived_html, name='archive'),
    
]