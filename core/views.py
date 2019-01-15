from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

# Crie suas views aqui.
def index(request):
    latest_Question_list = Question.objects.order_by('-data_public')[:5]
    #template= loader.get_template('core/index.html')
    context={'latest_Question_list': latest_Question_list,}
    return render(request, 'core/index.html',context)

def detail(request,Question_id):
    return HttpResponse("You're looking at questions %s."%Question_id)

def results(request,Question_id):
    response="You're looking at results of questions %s."
    return HttpResponse(response %Question_id)

def vote(request,Question_id):
    return HttpResponse("You're voting on questions %s."%Question_id)