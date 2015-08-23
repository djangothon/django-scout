# -*- coding: utf-8 -*-

import dropbox
from django.conf import settings
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from survey.models import *
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.response import Response
from serializers import *
from django.views.generic.base import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def create_survey(request):
	SurveyFormSet = modelformset_factory(Survey, fields=('title', 'description','questions','public'))
	if request.method == 'POST':
		formset = SurveyFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
	else:
		formset = SurveyFormSet()
  	return render_to_response("add_survey.html", {
			"title": "Add Survey",
	    "formset": formset,
	  })

class SurveyListView(generics.ListAPIView):
    serializer_class = SurveySerializer
    model = serializer_class.Meta.model
    queryset = Survey.objects.all()

class SurveyViewSet(viewsets.ModelViewSet):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()

class IntegerAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = IntegerAnswerSerializer
    queryset = IntegerAnswer.objects.all()

class TextAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = TextAnswerSerializer
    queryset = TextAnswer.objects.all()

class SurveyQuestionView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    
    def get_queryset(self):
        survey = self.request.query_params.get('uid')
        return Question.objects.filter(survey__uid=survey)
        
#class ConnectDropbox(View):

class NumResponseView(View):
    def get(self, request, uid):
        print uid
        return HttpResponse(BaseAnswer.objects.filter(question__survey__uid = uid).count())

class RecordAnswerView(generics.CreateAPIView):
    pass

@csrf_exempt
def check_response(request):
    if request.method == 'POST':
        print request.POST
    return HttpResponse("Here");
