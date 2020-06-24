# Generated by Django 3.0.7 on 2020-06-24 00:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        ('celebs', '0002_auto_20200624_0040'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='pgrating',
            name='added_by',
            field=models.ForeignKey(blank=True, default=None, help_text='User who added the db record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies_pgrating_adders', to=settings.AUTH_USER_MODEL, verbose_name='added by'),
        ),
        migrations.AddField(
            model_name='pgrating',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=None, help_text='User who updated the db record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies_pgrating_modifiers', to=settings.AUTH_USER_MODEL, verbose_name='updated by'),
        ),
        migrations.AddField(
            model_name='moviecrew',
            name='crew',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moviecrews', to='celebs.Celebrity', verbose_name='crew'),
        ),
        migrations.AddField(
            model_name='moviecrew',
            name='duty',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='moviecrews', to='celebs.Duty', verbose_name='duty'),
        ),
        migrations.AddField(
            model_name='moviecrew',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moviecrews', to='movies.Movie', verbose_name='movie'),
        ),
        migrations.AddField(
            model_name='movie',
            name='added_by',
            field=models.ForeignKey(blank=True, default=None, help_text='User who added the db record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies_movie_adders', to=settings.AUTH_USER_MODEL, verbose_name='added by'),
        ),
        migrations.AddField(
            model_name='movie',
            name='crews',
            field=models.ManyToManyField(blank=True, related_name='movies', through='movies.MovieCrew', to='celebs.Celebrity', verbose_name='crews'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, related_name='movies', to='movies.Genre', verbose_name='genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='pg_rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies', to='movies.PgRating', verbose_name='PG rating'),
        ),
        migrations.AddField(
            model_name='movie',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=None, help_text='User who updated the db record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies_movie_modifiers', to=settings.AUTH_USER_MODEL, verbose_name='updated by'),
        ),
        migrations.AddField(
            model_name='genre',
            name='added_by',
            field=models.ForeignKey(blank=True, default=None, help_text='User who added the db record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies_genre_adders', to=settings.AUTH_USER_MODEL, verbose_name='added by'),
        ),
        migrations.AddField(
            model_name='genre',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=None, help_text='User who updated the db record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies_genre_modifiers', to=settings.AUTH_USER_MODEL, verbose_name='updated by'),
        ),
        migrations.AlterUniqueTogether(
            name='moviecrew',
            unique_together={('movie', 'list_order')},
        ),
    ]
