from django.contrib import admin

from .models import Question, Player, Player_Response
# Register your models here.

admin.site.register(Player)
admin.site.register(Question)
admin.site.register(Player_Response)
