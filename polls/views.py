from django.shortcuts import render, get_object_or_404
#from django.template import loader
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.views import generic
from django.utils import timezone

#Versão sem generic views
'''
# Create your views here. É sempre necessário uma request object

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.") ##this is my homepage, my first view
    
    #codigo antes de criar templates
    latest_question_list = Question.objects.order_by('-pub_date')[:5] #ordena o Objeto "question" por data. o "-" indica que a ordem é inversa 
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)*/ #codigo antes de criar templates

    #versao com template
    latest_question_list = Question.objects.order_by('-pub_date')[:5] 
    template = loader.get_template('polls/index.html') #chama o template
    context = {
        'latest_question_list': latest_question_list,  #context é passar do backend para o front baseado num contexto
    }
    return HttpResponse(template.render(context, request))

    #versao com a função 'loader' para chamar o template reduzida 
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) #colocamos o template direto no render

def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id)
    
    #versão de erro com http404
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
        #pass -> isso ignora o erro se aplicado

    #versão de erro com get_object_or_404()
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question}) #passamos o contexto 'question' direto no render

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

'''
class IndexView(generic.ListView):
    template_name = 'polls/index.html'  #O nome dessa variavel nao e aleatoria, precisa ser essa
    context_object_name = 'latest_question_list'

    #def get_queryset(self):
    #    """Return the last five published questions."""     #versao sem testes, nao valida datas futuras
    #    return Question.objects.order_by('-pub_date')[:5]
    
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) #'choice' é passado como dicionario, vindo do "form" em detail.htm que resulta no id da escolha.
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))