from django.contrib import admin

from .models import Question, Player, Player_Response
# Register your models here.


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobil_phone', 'city', 'team')

admin.site.register(Player, PlayerAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'answer', 'score')

admin.site.register(Question, QuestionAdmin)


class Player_ResponseAdmin(admin.ModelAdmin):
    list_display =('question_id', 'player_id', 'message', 'correct', 'winner')
    list_filter = ['correct', 'winner']

admin.site.register(Player_Response, Player_ResponseAdmin)

