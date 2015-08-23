from .utils import generate_uid
from django.db import models
from django.contrib.auth.models import User

class LatLngType(models.Model):
    latitude = models.CharField('Latitude', max_length=20, null=True, blank=True)
    longitude = models.CharField('Longitude', max_length=20, null=True, blank=True)

class AnswerType(models.Model):
    title = models.CharField(max_length=80)
    a_type = models.CharField(max_length=80)
    def __unicode__(self):
        return unicode(self.title)

class Question(models.Model):
    title = models.CharField(max_length=200)
    answer_type = models.ForeignKey(AnswerType)
    created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return unicode(self.title)
    

class Survey(models.Model):
    uid = models.CharField(max_length=15,unique=True, db_index=True)
    title = models.CharField( max_length=255)
    description= models.TextField(blank=True)
    public  = models.BooleanField()
    required  = models.BooleanField(default=True)
    owner = models.ForeignKey(User)
    questions = models.ManyToManyField(Question)
    created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return unicode(self.title)
    
    def check_unique(self,ext):
        try:
            surveys = Survey.objects.get(uid=ext)
        except Survey.DoesNotExist:
            return True
        return False

    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = generate_uid(self)
        super(Survey, self).save(*args, **kwargs)

class BaseAnswer(models.Model):
    uid = models.CharField(max_length=15,unique=True, db_index=True)
    participant  = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    created = models.DateTimeField(auto_now_add=True)
    
    def check_unique(self,ext):
        try:
            baseanswers = BaseAnswer.objects.get(uid=ext)
        except BaseAnswer.DoesNotExist:
            return True
        return False

    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = generate_uid(self)
        super(BaseAnswer, self).save(*args, **kwargs)

class PhotoAnswer(BaseAnswer):
    image_url = models.URLField()

class IntegerAnswer(BaseAnswer):
    number = models.IntegerField()

class TextAnswer(BaseAnswer):
    text = models.CharField(max_length=255)
