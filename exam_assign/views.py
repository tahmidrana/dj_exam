from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from exam_assign.models import ExamAssign
from datetime import datetime


def start_exam(request, id):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    exam_assign = ExamAssign.objects.get(pk=id)
    # exam_assign.started_on = current_datetime
    # exam_assign.save()
    context = {"exam_assign_detail": exam_assign}
    return render(request, "start_exam.html", context)
    # return HttpResponse("Exam started at %s" % current_datetime)


def enroll_exam(request, id):
    # exam_assign_detail = ExamAssign.objects.get(pk=id)
    exam_assign_detail = get_object_or_404(ExamAssign, pk=id)
    context = {"exam_assign_detail": exam_assign_detail}
    return render(request, "enroll_exam.html", context)
