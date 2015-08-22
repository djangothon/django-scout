from django.contrib import admin
from survey.models import *

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    #readonly_fields = ('uid',)

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner',)
    readonly_fields = ('uid',)

class AnswerTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)

class DropboxTokenAdmin(admin.ModelAdmin):
    list_display = ('user',)

class IntegerAnswerAdmin(admin.ModelAdmin):
    readonly_fields = ('uid',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(AnswerType, AnswerTypeAdmin)
admin.site.register(IntegerAnswer, IntegerAnswerAdmin)
admin.site.register(DropboxToken, DropboxTokenAdmin)
