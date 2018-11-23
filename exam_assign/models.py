from django.db import models
from django.contrib.auth.models import User
from exams.models import Exam


class ExamAssign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True)
    assigned_on = models.DateField(auto_now_add=True)
    started_on = models.DateField(null=True, blank=True)
    obtained_mark = models.IntegerField(null=True, blank=True)
