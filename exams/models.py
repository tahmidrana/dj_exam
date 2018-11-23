from django.db import models
from django.contrib.auth.models import User


class Exam(models.Model):
    title = models.CharField(max_length=250)
    duration = models.IntegerField()
    mark = models.IntegerField()
    pass_mark = models.IntegerField()
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=250)
    mark = models.IntegerField()
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title


class Answer(models.Model):
    title = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
