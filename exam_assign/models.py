from django.db import models
from django.contrib.auth.models import User
from exams.models import Exam, Question, Answer


class ExamAssign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True)
    assigned_on = models.DateField(auto_now_add=True)
    started_on = models.DateTimeField(null=True, blank=True)
    submitted_on = models.DateTimeField(null=True, blank=True)
    obtained_mark = models.IntegerField(null=True, blank=True)


class ExamAnswer(models.Model):
    exam_assign = models.ForeignKey(ExamAssign, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_ans = models.ForeignKey(Answer, on_delete=models.CASCADE)
