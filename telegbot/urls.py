from django.urls import path

from . import views

app_name = 'telegbot'
urlpatterns = [
    path('', views.index, name='index'),
    path('players', views.players, name = "players"),
    path('responses', views.player_response, name = "player_response")
]