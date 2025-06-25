from django.http import HttpResponse, HttpRequest
from .models import Question
from django.shortcuts import get_object_or_404, render
from django.http import Http404

def detail(request: HttpRequest, question_id: int):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request: HttpRequest, question_id: int):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request: HttpRequest, question_id: int):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request: HttpRequest):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)