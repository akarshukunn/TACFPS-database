# Generated by Django 4.1.2 on 2023-01-11 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_player_esports_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='esports_team',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.team'),
        ),
    ]
