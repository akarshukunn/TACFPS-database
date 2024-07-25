from django.db import models

# Create your models here.
class Game(models.Model):

    name = models.CharField(default="#", max_length=255)
    description = models.CharField(default="#", max_length=500)
    release = models.DateField()
    image = models.CharField(default="#", max_length=500, blank=True, null=True)
    developer = models.CharField(default="#", max_length=255)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(default="#", max_length=255)
    established = models.DateField()
    country = models.CharField(default="#", max_length=255)
    image = models.CharField(default="#", max_length=500, blank=True, null=True)
    players = models.ManyToManyField('Player')
    def __str__(self):
        return self.name

class Player(models.Model):
    first_name = models.CharField(default="#", max_length=255)
    last_name = models.CharField(default="#", max_length=255)
    image = models.CharField(default="#", max_length=500, blank=True, null=True)
    ign = models.CharField(default="#", max_length=255)

    bio = models.CharField(default="#", max_length=500)

    dob = models.DateField()

    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    esports_team = models.ForeignKey('Team', on_delete=models.CASCADE, blank=True, null=True)

    player_stats = models.OneToOneField('Stat', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.ign

class Stat(models.Model):
    for_player = models.CharField(default="#", max_length=255)
    kd = models.FloatField()
    rating = models.IntegerField()

    def __str__(self):
        return self.for_player

class Tournament(models.Model):
    name = models.CharField(default="#", max_length=255)
    location = models.CharField(default="#", max_length=255)
    date = models.DateField()
    image = models.CharField(default="#", max_length=500, blank=True, null=True)
    prize = models.CharField(default="#", max_length=255)

    participating_teams = models.ManyToManyField('Team')
    matches_played = models.ManyToManyField('Match')

    def __str__(self):
        return self.name

class Match(models.Model):
    match_name = models.CharField(default="#", max_length=255)
    tournament_played = models.ForeignKey('Tournament', on_delete=models.CASCADE, blank=True, null=True)

    team_1 = models.ForeignKey('Team', on_delete=models.CASCADE, blank=True, null=True, related_name='team_1')
    team_2 = models.ForeignKey('Team', on_delete=models.CASCADE, blank=True, null=True, related_name='team_2')

    winning_team = models.ForeignKey('Team', on_delete=models.CASCADE, blank=True, null=True, related_name='winning_team')

    def __str__(self):
        return self.match_name