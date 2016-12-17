from datetime import datetime

from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    question_title = models.CharField(max_length=200, blank=True)
    pub_date = models.DateField(default=datetime.now)


class Choice(models.Model):
    text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    news_id = models.ForeignKey(News)
