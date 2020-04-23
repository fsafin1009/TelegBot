from django.shortcuts import render

# Create your views here.
from telegbot.models import Question


def index(request):
    questions_list = Question.objects.all()
    context = {'questions_list': questions_list}
    return render(request, 'telegbot/index.html', context)