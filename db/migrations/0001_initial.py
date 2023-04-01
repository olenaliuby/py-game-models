# Generated by Django 4.0.2 on 2023-03-29 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('bonus', models.CharField(max_length=255, verbose_name='Describes what kind of bonus players can get from it')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='race_skills', to='db.race')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255)),
                ('bio', models.CharField(max_length=255, verbose_name='Stores a short description provided by a user about himself/herself.')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('guild', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='player_guild', to='db.guild')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='player_race', to='db.race')),
            ],
        ),
    ]