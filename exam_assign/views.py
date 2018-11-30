from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from exam_assign.models import ExamAssign, ExamAnswer
from exams.models import Question, Answer
from datetime import datetime
from django.contrib.auth.decorators import login_required


@login_required
def start_exam(request, id):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    exam_assign = ExamAssign.objects.get(pk=id)
    if not exam_assign.submitted_on:
        if not exam_assign.started_on:
            exam_assign.started_on = current_datetime
            exam_assign.save()
        context = {"exam_assign_detail": exam_assign}
        return render(request, "start_exam.html", context)
    else:
        return HttpResponse("<h1>You already submitted this exam</h1>")
    # return HttpResponse("Exam started at %s" % current_datetime)


@login_required
def enroll_exam(request, id):
    # exam_assign_detail = ExamAssign.objects.get(pk=id)
    exam_assign_detail = get_object_or_404(ExamAssign, pk=id)
    context = {"exam_assign_detail": exam_assign_detail}
    return render(request, "enroll_exam.html", context)


def submit_exam(request, id):
    exam_assign = ExamAssign.objects.get(pk=id)
    if exam_assign.started_on and not exam_assign.submitted_on:  # exam started already
        data = request.POST
        for x in data:
            if not str(x) == "csrfmiddlewaretoken":
                # ht += x.split("_")[2] + " : " + data[x] + "<br>"
                ques = x.split("_")[2]
                ans = data[x]
                exam_ans = ExamAnswer(
                    exam_assign=exam_assign,
                    question=Question.objects.get(pk=int(ques)),
                    user_ans=Answer.objects.get(pk=int(ans)),
                )
                exam_ans.save()  # save all the answer

                exam_assign.submitted_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                exam_assign.save()

    return HttpResponse("Exam Complete")
