from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import Question, Answer
from django.core.paginator import Paginator

# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def fail404(request, *args, **kwargs):
    return HttpResponseNotFound()

def new_questions(request, *args, **kwargs):
    questions = Question.objects.order_by('-id')
    limit = 10
    paginator = Paginator(questions, limit)

    page = request.Get.get('page', 1)
    page_obj = paginator.page(page)

    return render(request, 'qa/new_questions.html', {
        'questions_on_page' : page_obj.object_list
    })

def popular(request, *args, **kwargs):
    questions = Question.objects.popular()
    limit = 10
    paginator = Paginator(questions, limit)

    page = request.Get.get('page', 1)
    page_obj = paginator.page(page)

    return render(request, 'qa/popular_questions.html', {
        'questions_on_page' : page_obj.object_list
    })

def one_question(request, qid):
    quest = get_object_or_404(Question, pk=qid)
    answers = quest.answer_set.all()
    return render(request, 'qa/question.html', {
        "title" : quest.title,
        "text" : quest.text,
        "answers" : answers
    })
