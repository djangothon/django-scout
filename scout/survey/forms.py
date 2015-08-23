from django import forms
from django.forms import ModelForm
from survey.models import Survey, Question


class SurveyModelForm(ModelForm):
    class Meta:
        model = Survey

    uid = forms.CharField(required=False)

class QuestionModelForm(ModelForm):
    class Meta:
        model = Question

    uid = forms.CharField(required=False)
