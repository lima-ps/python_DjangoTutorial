import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):  #esse metodo vai permitir que quando o Objeto for chamado ele possa ser passado como string para o console.
        return self.question_text

    #versão com bug. Ele retorna True mesmo se for postado em data futura
    '''def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)'''

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
