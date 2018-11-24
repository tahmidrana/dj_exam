from django.shortcuts import render, get_object_or_404
from exam_assign.models import ExamAssign


def start_exam(request, id):
    pass


def enroll_exam(request, id):
    # exam_assign_detail = ExamAssign.objects.get(pk=id)
    exam_assign_detail = get_object_or_404(ExamAssign, pk=id)
    context = {"exam_assign_detail": exam_assign_detail}
    return render(request, "enroll_exam.html", context)
