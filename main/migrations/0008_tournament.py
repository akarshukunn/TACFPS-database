# Generated by Django 4.1.2 on 2023-01-11 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_stat_alter_player_game_player_player_stats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='#', max_length=255)),
                ('location', models.CharField(default='#', max_length=255)),
                ('date', models.DateField()),
                ('prize', models.CharField(default='#', max_length=255)),
                ('participating_teams', models.ManyToManyField(to='main.team')),
            ],
        ),
    ]
