from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
#from django.template import loader
from .models import Question

# Crie suas views aqui.
def index(request):
    ultima_questao = Question.objects.order_by('data_public')[:5]
    #template= loader.get_template('core/base.html')
    context={'ultima_questao': ultima_questao,}
    return render(request, 'core/base.html',context)

def detail(request,Question_id):
    questao=get_object_or_404(Question, teste=Question_id)
    return render(request, 'core/detail.html', {'Questao':questao})
    #try:
    #   questao = Question.objects.get(teste=Question_id)
    #except Question.DoesNotExist:
    #   raise Http404("Essa questão não existe")
    #return render(request, 'core/detail.html',{'Questao': questao})

def results(request,Question_id):
    response="You're looking at results of questions %s."
    return HttpResponse(response %Question_id)

def vote(request,Question_id):
    return HttpResponse("You're voting on questions %s."%Question_id)