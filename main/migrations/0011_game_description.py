# Generated by Django 4.1.2 on 2023-01-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_game_image_player_image_team_image_tournament_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.CharField(default='#', max_length=500),
        ),
    ]
