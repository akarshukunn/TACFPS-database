# Generated by Django 4.1.2 on 2023-01-11 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='#', max_length=255)),
                ('release', models.DateField()),
                ('developer', models.CharField(default='#', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='#', max_length=255)),
                ('last_name', models.CharField(default='#', max_length=255)),
                ('ign', models.CharField(default='#', max_length=255)),
                ('bio', models.CharField(default='#', max_length=500)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='#', max_length=255)),
                ('established', models.DateField()),
                ('country', models.CharField(default='#', max_length=255)),
                ('players', models.ManyToManyField(to='main.player')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='esports_team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.team'),
        ),
        migrations.AddField(
            model_name='player',
            name='game',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.game'),
        ),
    ]
