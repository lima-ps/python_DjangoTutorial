from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404
from .models import Question


# Create your views here. É sempre necessário uma request object
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.") ##this is my homepage, my first view
    
    #codigo antes de criar templates
    '''latest_question_list = Question.objects.order_by('-pub_date')[:5] #ordena o Objeto "question" por data. o "-" indica que a ordem é inversa 
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)*/''' #codigo antes de criar templates

    #versao com template
    '''latest_question_list = Question.objects.order_by('-pub_date')[:5] 
    template = loader.get_template('polls/index.html') #chama o template
    context = {
        'latest_question_list': latest_question_list,  #context é passar do backend para o front baseado num contexto
    }
    return HttpResponse(template.render(context, request))'''

    #versao com a função 'loader' para chamar o template reduzida 
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) #colocamos o template direto no render

def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id)
    
    #versão de erro com http404
    '''try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
        #pass -> isso ignora o erro se aplicado'''

    #versão de erro com get_object_or_404()
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question}) #passamos o contexto 'question' direto no render

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)