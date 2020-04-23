from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(verbose_name="Name", max_length=128)
    mobil_phone = models.CharField(verbose_name="Phone", max_length=20)
    city = models.CharField(verbose_name="City", max_length=128)
    team = models.CharField(verbose_name="Team",max_length=128)

    def __str__(self):
        return self.name

class Question(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=256)
    answer = models.CharField(max_length=128)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Player_Response(models.Model):
    player_id = models.ForeignKey(Player, verbose_name="Player name", on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, verbose_name="Question", on_delete=models.CASCADE)
    message = models.CharField(max_length=150, verbose_name="Response")
    correct = models.BooleanField(default='False')
    winner = models.BooleanField(default='False')

    def team_name(self):
        return self.player_id.team
    team_name.short_description = 'Team'

    def __str__(self):
        return self.question_id
