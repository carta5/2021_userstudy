from django.shortcuts import render
from django.urls import reverse_lazy
from django.templatetags.static import static

from django.conf import settings
from django.views.generic import TemplateView, CreateView, ListView
from django.views.generic.base import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from .lib import helper

from .models import Task 
from .models import Description
from .models import TaskAnswer
from .models import PreQuestionnaireAnswer
from .models import PostQuestionnaireAnswer
from .models import ExitQuestionnaireAnswer
from .models import SearchResult

#動画の内容
from .models import VideoContentCheck

from django.contrib.auth.models import User

from .forms import PreQuestionnaireAnswerForm
from .forms import PostQuestionnaireAnswerForm
from .forms import ExitQuestionnaireAnswerForm
from .forms import TaskAnswerForm
from .forms import VideoContentCheckForm


PROJECT_ID = "MS-M12020-{}".format(settings.RECRUIT_CODE)
TITLE = "ユーザ実験（{}）".format(PROJECT_ID)
TASK_NUM = 1
SITE_PATH = "https://xxxxxx.com"


# Create your views here.
class IndexView(TemplateView):
    template_name = "userstudy/templates/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = TITLE
        context['recruit_website'] = settings.RECRUIT_WEBSITE
        
        return context

class StartView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login'
    template_name = 'userstudy/templates/start.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = TITLE
        context['project_id'] = PROJECT_ID
        context['user_id'] = self.request.user.username

        return context

class ReadyView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login'
    template_name = 'userstudy/templates/ready.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_id'] = PROJECT_ID
        context['user_id'] = self.request.user.username
        context['title'] = "情報検索タスク"
        return context


class PreQuestionnaireView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    template_name = 'userstudy/templates/pre_questionnaire.html'

    model = PreQuestionnaireAnswer
    form_class = PreQuestionnaireAnswerForm
    success_url = reverse_lazy('userstudy:task_introduction_1')

    #ここでの回答に応じて被験者を分けるコード
    #1:ネガティブ 2:バイアスなし 3:ポジティブ
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = TITLE
        context['project_id'] = PROJECT_ID
        context['user_id'] = self.request.user.username
        return context

    def form_valid(self, form):
        user_obj = User.objects.get(pk=self.request.user.pk)
        form.instance.participant = user_obj
        
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

#検索タスクの最初
class TaskIntroductionFirstView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login'
    template_name = 'userstudy/templates/task_introduction_1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_id'] = PROJECT_ID
        context['user_id'] = self.request.user.username
        
        #taskの導入文は同じなのでid=1
        task = Task.objects.get(id=1)
        #シナリオを保存
        context["task_scenario"] = task.scenario
        return context

# #検索タスクの2番目
class TaskIntroductionSecondView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login'
    template_name = 'userstudy/templates/task_introduction_2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_id'] = PROJECT_ID
        context['user_id'] = self.request.user.username

        #idで抽出する
        pre_questionnaires = PreQuestionnaireAnswer.objects.filter(participant_id=self.request.user.id)
        
        #アンケート内容を降順したあとfor文で回す
        order_pre_questionnaires  = pre_questionnaires.order_by("updated_at").reverse()
        
        #リストの初期化
        prior_belief_list = []
      
        #リストの先頭を取り，最新の値を取得
        prior_belief = prior_belief_list[0].prior_belief
        
        #まずタスクのグループを振り分けるためのidを初期化
        task_group_id = 0

        #アンケート内容に応じて条件分岐(1:ネガティブ,2:バイアスなし,3:ポジティブ）
        if prior_belief == 1 or prior_belief == 2:
            task_group_id = 1
        elif prior_belief == 3:
            task_group_id = 2
        elif prior_belief == 4 or prior_belief == 5:
            task_group_id = 3
        else:
            print("エラー")

        description = Description.objects.get(id=task_group_id)

        #事前情報1をcontextに保存
        context['additional_scenario_1'] = description.infomation_1
        
        #セッションを利用してtask_group_idを保存する
        self.request.session["task_group_id"] = task_group_id

        return context


# #検索タスクの3番目（事前情報2を表示）
class TaskIntroductionThirdView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    template_name = 'userstudy/templates/task_introduction_3.html'

    #動画内容の確認のために追加
    model = VideoContentCheck
    form_class = VideoContentCheckForm
    success_url = reverse_lazy('userstudy:task_introduction_4')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_id'] = PROJECT_ID
        context['user_id'] = self.request.user.username

        #セッションを利用してtask_group_idを取得
        task_group_id = self.request.session["task_group_id"]
        description = Description.objects.get(id=task_group_id)

        #コンテキストに事前情報2を保存
        context['additional_scenario_2'] = description.infomation_2
        
        return context
    
    #動画内容をまとめる質問
    def form_valid(self, form):
        user_obj = User.objects.get(pk=self.request.user.pk)
        form.instance.participant = user_obj
        print(form)
        
        return super().form_valid(form)

# 動画を見たあとにその内容をチェックする
class VideoContentCheckView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    template_name = 'userstudy/templates/video_content_questionnaire.html'

    model = VideoContentCheck
    form_class = VideoContentCheckForm
    success_url = reverse_lazy('userstudy:task_introduction_4')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_id'] = PROJECT_ID
        context['user_id'] = self.request.user.username

        return context

    def form_valid(self, form):
        user_obj = User.objects.get(pk=self.request.user.pk)
        form.instance.participant = user_obj
        print(form)
        return super().form_valid(form)

# #検索タスクの4番目（検索タスクを行う）
class TaskIntroductionFourthView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    template_name = 'userstudy/templates/task_introduction_4.html'

    model = TaskAnswer
    form_class = TaskAnswerForm
    success_url = reverse_lazy('userstudy:post_questionnaire')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_id'] = PROJECT_ID
        context['user_id'] = self.request.user.username

        #セッションを利用してtask_group_idを取得
        task_group_id = self.request.session["task_group_id"]
        description = Description.objects.get(id=task_group_id)

        #コンテキストに事前情報3を保存
        context['additional_scenario_3'] = description.infomation_3
        return context

    def form_valid(self, form):
        user_obj = User.objects.get(pk=self.request.user.pk)
        task_group_id = self.request.session["task_group_id"]
        task_obj = Task.objects.get(pk=task_group_id)

        form.instance.participant = user_obj
        form.instance.task = task_obj
        return super().form_valid(form)


#事前アンケート
class PostQuestionnaireView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    template_name = 'userstudy/templates/post_questionnaire.html'

    model = PostQuestionnaireAnswer
    form_class = PostQuestionnaireAnswerForm
    success_url = reverse_lazy('userstudy:exit_questionnaire')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_id'] = PROJECT_ID
        context['user_id'] = self.request.user.username
        context['title'] = "情報検索タスク(4/4)"
        return context

    def form_valid(self, form):
        user_obj = User.objects.get(pk=self.request.user.pk)
        task_group_id = self.request.session["task_group_id"]
        task_obj = Task.objects.get(pk=task_group_id)
        form.instance.participant = user_obj
        form.instance.task = task_obj
        
        return super().form_valid(form)

class ExitQuestionnaireAnswerView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    template_name = 'userstudy/templates/exit_questionnaire.html'

    model = ExitQuestionnaireAnswer
    form_class = ExitQuestionnaireAnswerForm
    success_url = reverse_lazy('userstudy:complete')

    def form_valid(self, form):
        user_obj = User.objects.get(pk=self.request.user.pk)
        task_group_id = self.request.session["task_group_id"]
        task_obj = Task.objects.get(pk=task_group_id)
        form.instance.participant = user_obj
        form.instance.task = task_obj
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "事後アンケート"
        return context

class WorkCompletionView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login'
    template_name = 'userstudy/templates/work_completion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_id'] = PROJECT_ID
        context['user_id'] = self.request.user.username
        
        #タスクの完了コードを発行（固定）
        fixed_str = "BzMzxEdMVz7vtIlrIVgQ"
        completion_code = PROJECT_ID + ':' + fixed_str
        print(completion_code)

        context['title'] = "情報検索タスク - お疲れ様でした"
        context['completion_code'] = completion_code
        context['recruit_website'] = settings.RECRUIT_WEBSITE

        return context

class SearchResultListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    model = SearchResult
    context_object_name = 'search_result_list'
    template_name = 'searchresult_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

      
        context['project_id'] = PROJECT_ID
        context['user_id'] = self.request.user.username
        return context

    #ランクを昇順にして返す
    def get_queryset(self):

        #昇順にして返す
        return SearchResult.objects.order_by('rank')


#../archiveにhtmlファイルを入れてそれを表示する
def show_archived_html(request, page_id):
    template_path = 'userstudy/archive/{}.html'.format(page_id)
    css_tag = "<link rel=\"stylesheet\" type=\"text/css\" href=\"{}{}\" />".format(SITE_PATH, static('css/archive.css'))

    script_tag = """
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="{site_path}{js_path}/browser-polyfill.min.js"></script>
<script src="{site_path}{js_path}/userbehavior.js"></script>
<script src="{site_path}{js_path}/helper.js"></script>
<script src="{site_path}{js_path}/browsing-monitor.js"></script>
<script type="text/javascript">
    let projectID = '{project_id}';
    let userID = '{user_id}';
</script>
""".format(js_path=static('js'), project_id=PROJECT_ID,
           user_id=request.user.username, site_path=SITE_PATH)

    context = {'head': css_tag + script_tag}
    return render(request, template_path, context)
