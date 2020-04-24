from django.shortcuts import render

# Create your views here.


from telegbot.models import Question, Player, Player_Response


def index(request):
    questions_list = Question.objects.all()
    context = {'questions_list': questions_list}
    return render(request, 'telegbot/index.html', context)

# class PlayerView(generic.ListView):
#     model = Player
#     template_name = 'telegbot/players.html'
#     def get_queryset(self):
#         return Player.objects.all()

def players(request):
    player_list = Player.objects.all()
    context = {'player_list': player_list}
    return render(request, 'telegbot/players.html', context)

def player_response(request):
    player_response_list = Player_Response.objects.all()
    context = {'player_response_list': player_response_list}
    return render(request, 'telegbot/player_response.html', context)

