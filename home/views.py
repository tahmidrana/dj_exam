from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from exams.models import Exam
from exam_assign.models import ExamAssign, ExamAnswer


def my_exam_list(request):
    if not request.user.is_authenticated:
        exam_list = None
    else:
        exam_list = ExamAssign.objects.filter(user=request.user).order_by("-id")
    context = {"user_exam_list": exam_list}
    return render(request, "exam_list.html", context)


def exam_result(request, id):
    exam_assign = get_object_or_404(ExamAssign, pk=id)
    if exam_assign.submitted_on:
        exam_answers = ExamAnswer.objects.filter(exam_assign=exam_assign)
        context = {"exam_assign_detail": exam_assign, "exam_answers": exam_answers}
        return render(request, "exam_result.html", context)
    else:
        return HttpResponse("Please complete and submit the exam first")
