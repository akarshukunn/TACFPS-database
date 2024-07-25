from django.shortcuts import render
from .models import Game, Player, Team, Tournament
# Create your views here.
def home(request):

    games = Game.objects.all()

    obj = {
        'games': games
    }

    return render(request, 'index.html', obj)

def game(request, game_id):
    game = Game.objects.get(id=game_id)
    players = Player.objects.filter(game=game_id)
    
    obj = {
        'game': game,
        'players': players
    }
    return render(request, 'game.html', obj)

def player(request, player_id):

    player_selected = Player.objects.get(id=player_id)
    print(player_selected.player_stats)
    obj = {
        'player':player_selected
    }

    return render(request, 'player.html', obj)

def players(request):
    players = Player.objects.all()
    obj = {
        'players': players
    }
    return render(request, 'players.html', obj)

def teams(request):
    teams = Team.objects.all()
    obj = {
        'teams': teams 
    }
    return render(request, 'teams.html', obj)

def team(request, team_id):
    team = Team.objects.get(id=team_id)

    players = team.players.all()
    
    obj = {
        'team': team,
        'players': players
    }
    return render(request, 'team.html', obj)

def tournaments(request):
    tournaments = Tournament.objects.all()

    obj = {
        'tournaments': tournaments
    }

    return render(request, 'tournaments.html', obj)

def tournament(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    teams = tournament.participating_teams.all()
    matches = tournament.matches_played.all()
    
    obj = {
        'tournament': tournament,
        'teams': teams,
        'matches': matches
    }

    return render(request, 'tournament.html', obj)
