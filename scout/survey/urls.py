# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from views import *

router = DefaultRouter()
router.register(r'survey', SurveyViewSet)
router.register(r'intanswer', IntegerAnswerViewSet)
router.register(r'textanswer', TextAnswerViewSet)

urlpatterns = patterns('',
        url(r'^', include(router.urls)),
	url(r'^add$', create_survey),
	url(r'^survey$', SurveyListView.as_view()),
	url(r'^numresponse/(?P<uid>[a-zA-Z0-9]+)/$', NumResponseView.as_view()),
	url(r'^questions/$', SurveyQuestionView.as_view()),
	url(r'^check/$', check_response),
	#url(r'^dropbox/connect$', ConnectDropbox.as_view()),
        
)
