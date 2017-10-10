from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Question, Answer
from django.core.paginator import Paginator

# Create your views here.
def test(request, *args, **kwargs):
    # return render(request, 'some.html', {})
    return HttpResponse('OK')

def fail404(request, *args, **kwargs):
    return HttpResponseNotFound()

def new_questions(request, *args, **kwargs):
    questions = Question.objects.new_by_id()
    limit = 10
    paginator = Paginator(questions, limit)

    page = request.Get.get('page', 1)
    paginator.baseurl = '/question/'
    page_obj = paginator.page(page)
    return render(request, 'qa/new_questions.html', {
        'questions_on_page' : page_obj.object_list,
        'paginator' : paginator,
        'page': page
    })

def popular(request, *args, **kwargs):
    questions = Question.objects.popular()
    limit = 10
    paginator = Paginator(questions, limit)

    page = request.Get.get('page', 1)
    page_obj = paginator.page(page)
    return render(request, 'qa/popular_questions.html', {
        'questions_on_page' : page_obj.object_list,
        'paginator' : paginator,
        'page': page
    })

def one_question(request, qid):
    try:
        quest = Question.objects.get(pk=qid)
        return render(request, 'qa/question.html', {
            "title" : quest.title,
            "text" : quest.text,
            "answers" : Answer.objects.filter(question = qid)
        })
    except:
        return HttpResponseNotFound()