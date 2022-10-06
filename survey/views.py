from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Survey


def index(request):
    survey_list = Survey.objects.order_by('-pub_date')
    print(survey_list)
    context = {'survey_list': survey_list}
    return render(request, 'survey/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at questions %s" % question_id)

def results(request, question_id):
    response = "You're looking at the results of questions %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
# Create your views here.
