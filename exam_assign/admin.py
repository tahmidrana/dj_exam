from django.contrib import admin
from exam_assign.models import ExamAssign, ExamAnswer


class ExamAssignAdmin(admin.ModelAdmin):
    list_display = ("exam", "user", "assigned_on", "started_on", "obtained_mark")


admin.site.register(ExamAssign, ExamAssignAdmin)


class ExamAnswerAdmin(admin.ModelAdmin):
    list_display = ("exam_assign", "question", "user_ans")


admin.site.register(ExamAnswer, ExamAnswerAdmin)

