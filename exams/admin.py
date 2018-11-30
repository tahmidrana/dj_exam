from django.contrib import admin
from exams.models import Exam, Question, Answer


class ExamAdmin(admin.ModelAdmin):
    list_display = ("title", "duration", "mark", "pass_mark")


admin.site.register(Exam, ExamAdmin)
admin.site.register(Question)
admin.site.register(Answer)
