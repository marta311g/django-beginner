from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .Person import Person
from .models import Question
# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]

    jay = Person("bolt://localhost:7687", "Jay", 1989)
    users_in_db = jay.num_users()

    context = {'latest_questions': latest_questions, 'users_in_db': users_in_db}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question.objects.get(pk = question_id))
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {'question': question,'error_message': "Please select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args={question_id,}))