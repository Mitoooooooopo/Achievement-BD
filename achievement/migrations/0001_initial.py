# Generated by Django 5.1.4 on 2025-04-30 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bd_models', '0002_move_upload_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('achievement_emoji_id', models.BigIntegerField(blank=True, help_text='Discord emoji ID for achievement', null=True)),
                ('description', models.TextField()),
                ('enable', models.BooleanField(default=True, help_text='on or off the achievements')),
                ('required_balls', models.ManyToManyField(help_text='Which countryballs you need to collect', related_name='achievements', to='bd_models.ball')),
            ],
            options={
                'db_table': 'achievements',
            },
        ),
        migrations.CreateModel(
            name='PlayerAchievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unlocked_at', models.DateTimeField(auto_now_add=True)),
                ('achievement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_achievements', to='achievement.achievement')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_achievements', to='bd_models.player')),
            ],
            options={
                'verbose_name': 'Player Achievement',
                'verbose_name_plural': 'Player Achievements',
                'db_table': 'player_achievement',
                'unique_together': {('player', 'achievement')},
            },
        ),
    ]
