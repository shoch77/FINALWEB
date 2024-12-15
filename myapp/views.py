from django.shortcuts import render
from .models import Game

def home(request):
    return render(request, 'home.html')

def list_games(request):
    games = Game.objects.all()  
    return render(request, 'list_games.html', {'games': games})