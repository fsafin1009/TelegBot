from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(verbose_name="Enter your name", max_length=128)
    mobil_phone = models.CharField(verbose_name="Enter your phone", max_length=20)
    city = models.CharField(verbose_name="Enter your city", max_length=128)
    team = models.CharField(verbose_name="Enter your team",max_length=128)

    def __str__(self):
        return self.name

class Question(models.Model):
    title = models.TextField(max_length=256)
    answer = models.CharField(max_length=128)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Player_Response(models.Model):
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    message = models.CharField(max_length=150)
    correct = models.BooleanField(default='False')
    winner = models.BooleanField(default='False')
