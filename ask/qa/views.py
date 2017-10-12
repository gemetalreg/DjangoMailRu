from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from .models import Question, Answer
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.http import require_GET
from .forms import AskForm, AnswerForm

# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def fail404(request, *args, **kwargs):
    return HttpResponseNotFound()

def get_page(request):
    try:
        page_str = request.GET.get('page', 1)
        page = int(page_str)
        return page
    except ValueError:
        raise Http404

def get_page_obj(paginator, page):
    try:
        page_obj = paginator.page(page)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    finally:
        return page_obj

@require_GET
def new_questions(request, *args, **kwargs):
    questions = Question.objects.order_by('-id')
    limit = 10
    paginator = Paginator(questions, limit)

    page = get_page(request)
    page_obj = get_page_obj(paginator, page)

    return render(request, 'qa/new_questions.html', {
        'questions' : page_obj
    })

@require_GET
def popular(request, *args, **kwargs):
    questions = Question.objects.order_by('-rating')
    limit = 10
    paginator = Paginator(questions, limit)

    page = get_page(request)
    page_obj = get_page_obj(paginator, page)

    return render(request, 'qa/popular_questions.html', {
        'questions' : page_obj
    })

def one_question(request, qid):
    # fork for both POST and GET
    quest = get_object_or_404(Question, pk=qid)
    answers = quest.answer_set.all()
    form = AnswerForm(initial={'question': qid})
    params = {
        "title" : quest.title,
        "text" : quest.text,
        "answers" : answers,
        "question" : quest,
        "form" : form
    }
    return render(request, 'qa/question.html', params)

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            askModel = form.save()
            url = askModel.get_url()
            return HttpResponseRedirect(url)
        else:
            return render(request, 'qa/ask.html', {
            'form' : form
        })
    else:
        # request.method == "GET"
        empty_form = AskForm()
        return render(request, 'qa/ask.html', {
            'form' : empty_form
        })

def answer(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answerModel = form.save()
            url = answerModel.get_url()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect('/')

