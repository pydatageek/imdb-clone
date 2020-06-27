# Generated by Django 3.0.7 on 2020-06-26 15:30

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import movies.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(editable=False, verbose_name='added date')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='updated date')),
                ('name', models.CharField(max_length=245, unique=True, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='slug')),
                ('code', models.CharField(max_length=3, verbose_name='code')),
                ('content', models.CharField(blank=True, default='', max_length=250, verbose_name='content')),
                ('extra_chars_count', models.PositiveSmallIntegerField(default=0, editable=False, help_text='there is no need for extra chars for slug of this model             and if no need for it to be editable also.', verbose_name='extra characters count')),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(editable=False, verbose_name='added date')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='updated date')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='slug')),
                ('extra_chars_count', models.PositiveSmallIntegerField(default=5, help_text='The number of extra random characters be suffixed \n        to slug if needed. default is 0 and it means no extra chars.', validators=[django.core.validators.MaxValueValidator(9, message='max value is 9')], verbose_name='extra characters count')),
                ('name', models.CharField(max_length=245, unique=True, verbose_name='title')),
                ('original_name', models.CharField(blank=True, default='', max_length=245, verbose_name='original title')),
                ('is_featured', models.BooleanField(default=False, verbose_name='featured')),
                ('release_year', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1100), django.core.validators.MaxValueValidator(2100)], verbose_name='release year')),
                ('duration', models.PositiveSmallIntegerField(blank=True, default=0, help_text='in minutes', verbose_name='duration')),
                ('imdb_rating', models.FloatField(blank=True, default=0, help_text='e.g. 6.8', verbose_name='IMDB rating')),
                ('content', ckeditor.fields.RichTextField(blank=True, default='', verbose_name='content')),
                ('content_source', models.URLField(blank=True, default='', verbose_name='content source')),
                ('trailer', models.URLField(blank=True, default='', help_text='trailer url (ONLY for youtube videos yet)', verbose_name='trailer')),
                ('trailer_info', models.CharField(blank=True, default='', max_length=250, verbose_name='trailer info')),
                ('image', models.ImageField(blank=True, null=True, upload_to=movies.models.movie_directory_path, verbose_name='image')),
                ('image_credit', models.CharField(blank=True, default='', max_length=250, verbose_name='image credit')),
            ],
            options={
                'verbose_name': 'movie',
                'verbose_name_plural': 'movies',
                'ordering': ('-added_at', '-release_year', 'name'),
            },
        ),
        migrations.CreateModel(
            name='MovieCrew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, default='', help_text='e.g. short story, screenplay for writer or voice for cast', max_length=75, verbose_name='role')),
                ('screen_name', models.CharField(blank=True, default='', help_text="crew's name on movie", max_length=75, verbose_name='screen name')),
                ('list_order', models.PositiveSmallIntegerField(help_text='order of appearance on movie. normal appearance should             be producer(s) > director(s) > writer(s) > cast(s)', validators=[django.core.validators.MinValueValidator(1)], verbose_name='list order')),
            ],
            options={
                'verbose_name': 'movie crew',
                'verbose_name_plural': 'movie crews',
                'ordering': ('-movie__release_year', 'movie', 'list_order'),
            },
        ),
        migrations.CreateModel(
            name='PgRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(editable=False, verbose_name='added date')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='updated date')),
                ('name', models.CharField(max_length=245, unique=True, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='slug')),
                ('code', models.CharField(max_length=5, verbose_name='code')),
                ('content', models.CharField(blank=True, default='', max_length=250, verbose_name='content')),
                ('extra_chars_count', models.PositiveSmallIntegerField(default=0, editable=False, help_text='there is no need for extra chars for slug of this model             and if no need for it to be editable also.', verbose_name='extra characters count')),
            ],
            options={
                'verbose_name': 'PG Rating',
                'verbose_name_plural': 'PG Ratings',
                'ordering': ('pk',),
            },
        ),
    ]
