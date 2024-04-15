from django.shortcuts import render

from django.template import loader
# Create your views here.
from django.http import HttpResponse

from .models import Question

from django.http import Http404

from django.shortcuts import get_object_or_404, render

def detail_alt(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # Intenta obtener la pregunta con el ID proporcionado
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        # Si la pregunta no existe, lanza una excepción Http404
        raise Http404("La pregunta no existe")
    
    # Si se obtiene la pregunta correctamente, renderiza la plantilla detail.html
    return render(request, "polls/detail.html", {"question": question})


def index_template(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)