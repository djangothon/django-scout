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
	fields = ('id','uid','title', 'owner', 'description', 'questions')

class BaseAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BaseAnswer

class IntegerAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = IntegerAnswer

class TextAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TextAnswer
