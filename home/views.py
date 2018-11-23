from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from exams.models import Exam
from exam_assign.models import ExamAssign


def my_exam_list(request):
    if not request.user.is_authenticated:
        exam_list = None
    else:
        exam_list = ExamAssign.objects.filter(user=request.user)
    context = {
        'user_exam_list': exam_list
    }
    return render(request, 'exam_list.html', context)
