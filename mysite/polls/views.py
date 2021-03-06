from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .Person import Request
from .models import Question
# Create your views here.

def index(request):
    #latest_questions = Question.objects.order_by('-pub_date')[:5]
    mydict = {
        "datetime": "30/Aug/2020:03:24:31"
    }
    print(test('Request', mydict))

    my_request = Request('req1', '30/Aug/2020:03:24:31', '+0200', 'GET', '/education', '200')
    #request_result = create_request(my_request)

    context = {'request_result': request_result}
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