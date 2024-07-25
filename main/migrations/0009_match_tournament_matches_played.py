# Generated by Django 4.1.2 on 2023-01-11 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_tournament'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_name', models.CharField(default='#', max_length=255)),
                ('team_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_1', to='main.team')),
                ('team_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_2', to='main.team')),
                ('tournament_played', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.tournament')),
                ('winning_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winning_team', to='main.team')),
            ],
        ),
        migrations.AddField(
            model_name='tournament',
            name='matches_played',
            field=models.ManyToManyField(to='main.match'),
        ),
    ]