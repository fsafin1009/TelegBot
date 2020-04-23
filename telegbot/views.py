from django.shortcuts import render

# Create your views here.
from telegbot.models import Question, Player


def index(request):
    questions_list = Question.objects.all()
    context = {'questions_list': questions_list}
    return render(request, 'telegbot/index.html', context)


def detail(request):
    player_list = Player.objects.all()
    context = {'player_list': player_list}
    return render(request, 'telegbot/detail.html', context)
