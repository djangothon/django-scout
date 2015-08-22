from models import *
from rest_framework import serializers

class AnswerTypeSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = AnswerType

class QuestionSerializer(serializers.ModelSerializer):
    answer_type = AnswerTypeSerializer()     
    class Meta:
        model = Question
        fields = ('title', 'answer_type')

class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = Survey
	fields = ('id','title', 'owner', 'description', 'questions')
