from django.urls import path
from .views import (
    home, 
    game, 
    player, 
    players, 
    teams, 
    team, 
    tournaments, 
    tournament
)

urlpatterns = [
    path('', home, name='home'),
    path('game/<int:game_id>', game, name='game'),
    path('player/<int:player_id>', player, name='player'),
    path('players/', players, name='players'),
    path('teams/', teams, name='teams'),
    path('team/<int:team_id>', team, name='team'),
    path('tournaments/', tournaments, name='tournaments'),
    path('tournament/<int:tournament_id>', tournament, name='tournament')
]