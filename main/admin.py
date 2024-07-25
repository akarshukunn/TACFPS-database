from django.contrib import admin
from .models import Game, Player, Team, Stat, Tournament, Match

# Register your models here.
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Stat)
admin.site.register(Tournament)
admin.site.register(Match)