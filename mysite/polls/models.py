import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) #label? UPDATE nei ég not þetta í shell og set inn choice text
    pub_date = models.DateTimeField('date published') #DateTimeField --- meira um þetta í tut2 (models)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()

        notInFuture = self.pub_date <= now
        inPastDay = self.pub_date >= now - datetime.timedelta(days=1) 
        return (notInFuture and inPastDay)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
        
        #now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200) #label? UPDATE nei ég not þetta í shell og set inn choice text
    votes = models.IntegerField(default=0) #IntegerField --- meira um þetta í tut2 (models)
    def __str__(self):
        return self.choice_text