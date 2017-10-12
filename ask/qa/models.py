from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# class QuestionManager(models.Manager):
#     def new(self):
#         return self.order_by('-added_at')
#
#     def new_id(self):
#         return self.order_by('-id')
#
#     def popular(self):
#         return self.order_by('-rating')


class Question(models.Model):
    # objects = QuestionManager()

    title = models.CharField(max_length = 255)
    text = models.TextField()
    added_at = models.DateField(blank=True, auto_now_add=True)
    rating = models.IntegerField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_like_user')

    def __unicode__(self):
        return self.title

    def get_url(self):
        return "/question/%s/" % self.pk

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(blank=True, auto_now_add = True)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __unicode__(self):
        return self.text

