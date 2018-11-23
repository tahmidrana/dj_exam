from django.contrib import admin
from exams.models import Exam, Question, Answer


admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Answer)
