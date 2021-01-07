from django import forms

from .models import TaskAnswer
from .models import PreQuestionnaireAnswer,PostQuestionnaireAnswer
#from .models import PostQuestionnaireAnswer
from .models import ExitQuestionnaireAnswer
from .models import VideoContentCheck

KNOWLEDGE_CHOICES = (
    (1, 'まったく知識がない'),
    (2, 'あまり知識がない'),
    (3, 'どちらでもない'),
    (4, 'かなり知識がある'),
    (5, '十分に知識がある'),
)

ANSWER_CHOICES = (
    (1, '危険である'),
    (2, '少し危険である'),
    (3, 'どちらでもない'),
    (4, '少し安全である'),
    (5, '安全である'),
)

E_HEALTH_LITERACY_CHOICES = (
    (1, '全くそう思わない'),
    (2, 'あまりそう思わない'),
    (3, 'どちらとも言えない'),
    (4, 'ややそう思う'),
    (5, 'かなりそう思う'),
)

EFFORT_CHOICES = (
    (1, '1分未満'),
    (2, '1〜2分'),
    (3, '2〜3分'),
    (4, '4〜5分'),
    (5, '6〜7分'),
    (6, '7〜8分'),
    (7, '8〜9分'),
    (8, '10分以上'),
)

METRIC_IMPORTANCE = (
    (1, 'まったく重視しなかった'),
    (2, 'あまり重視しなかった'),
    (3, 'そこそこ重視した'),
    (4, 'かなり重視した'),
    (5, '大いに重視した'),
)

SEX_CHOICES = (
    (0, '答えたくない'),
    (1, '男性'),
    (2, '女性'),
)

AGE_CHOICES = (
    (0, '答えたくない'),
    (1, '10代'),
    (2, '20代'),
    (3, '30代'),
    (4, '40代'),
    (5, '50代'),
    (6, '60歳以上'),
)

EDUCATION_CHOICES = (
    (0, '答えたくない'),
    (1, '中学校'),
    (2, '高校'),
    (3, '専門学校'),
    (4, '短大'),
    (5, '高専'),
    (6, '大学'),
    (7, '大学院'),
)

class PreQuestionnaireAnswerForm(forms.ModelForm):

    class Meta:
        model = PreQuestionnaireAnswer
        #fields = ['knowledge', 'prior_belief', 'spammer_check']
        fields = ['knowledge', 'prior_belief']
        widgets = {
            'knowledge': forms.RadioSelect(choices=KNOWLEDGE_CHOICES),
            'prior_belief': forms.RadioSelect(choices=ANSWER_CHOICES),
            #'spammer_check': forms.RadioSelect(choices=SPAMMER_CHECK),
        }

#動画の内容をチェックするテーブル
class VideoContentCheckForm(forms.ModelForm):

    class Meta:
        model = VideoContentCheck
        fields = ['video_content']
  

class TaskAnswerForm(forms.ModelForm):

    class Meta:
        model = TaskAnswer
        fields = ['answer', 'reason','url']
        widgets = {
            'answer': forms.RadioSelect(choices=ANSWER_CHOICES),
        }


class PostQuestionnaireAnswerForm(forms.ModelForm):

    class Meta:
        model = PostQuestionnaireAnswer
        fields = ['effort', 'evidence_existence',
                  'freshness', 'comprehensibility', 'source_expertise',
                  'aesthetics', 'content_coverage']
        widgets = {
            'effort': forms.RadioSelect(choices=EFFORT_CHOICES),
            'source_expertise': forms.RadioSelect(choices=METRIC_IMPORTANCE),
            'evidence_existence': forms.RadioSelect(choices=METRIC_IMPORTANCE),
            'freshness': forms.RadioSelect(choices=METRIC_IMPORTANCE),
            'comprehensibility': forms.RadioSelect(choices=METRIC_IMPORTANCE),
            'aesthetics': forms.RadioSelect(choices=METRIC_IMPORTANCE),
            'content_coverage': forms.RadioSelect(choices=METRIC_IMPORTANCE),
        }


class ExitQuestionnaireAnswerForm(forms.ModelForm):

    class Meta:
        model = ExitQuestionnaireAnswer
        fields = ['sex', 'age', 'education',
                  'e_health_literacy_q1', 'e_health_literacy_q2',
                  'e_health_literacy_q3', 'e_health_literacy_q4',
                  'e_health_literacy_q5', 'e_health_literacy_q6',
                  'e_health_literacy_q7', 'e_health_literacy_q8',
                  ]
        widgets = {
            'sex': forms.RadioSelect(choices=SEX_CHOICES),
            'age': forms.RadioSelect(choices=AGE_CHOICES),
            'education': forms.RadioSelect(choices=EDUCATION_CHOICES),
            'e_health_literacy_q1': forms.RadioSelect(choices=E_HEALTH_LITERACY_CHOICES),
            'e_health_literacy_q2': forms.RadioSelect(choices=E_HEALTH_LITERACY_CHOICES),
            'e_health_literacy_q3': forms.RadioSelect(choices=E_HEALTH_LITERACY_CHOICES),
            'e_health_literacy_q4': forms.RadioSelect(choices=E_HEALTH_LITERACY_CHOICES),
            'e_health_literacy_q5': forms.RadioSelect(choices=E_HEALTH_LITERACY_CHOICES),
            'e_health_literacy_q6': forms.RadioSelect(choices=E_HEALTH_LITERACY_CHOICES),
            'e_health_literacy_q7': forms.RadioSelect(choices=E_HEALTH_LITERACY_CHOICES),
            'e_health_literacy_q8': forms.RadioSelect(choices=E_HEALTH_LITERACY_CHOICES),
        }
