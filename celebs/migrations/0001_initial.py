# Generated by Django 3.0.7 on 2020-06-24 00:40

import celebs.models
import ckeditor.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(editable=False, verbose_name='added date')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='updated date')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='slug')),
                ('extra_chars_count', models.PositiveSmallIntegerField(default=5, help_text='The number of extra random characters be suffixed \n        to slug if needed. default is 0 and it means no extra chars.', validators=[django.core.validators.MaxValueValidator(9, message='max value is 9')], verbose_name='extra characters count')),
                ('name', models.CharField(blank=True, editable=False, help_text='computed full name', max_length=245, verbose_name='full name')),
                ('first_name', models.CharField(max_length=75, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, default='', max_length=75, verbose_name='last name')),
                ('nick_name', models.CharField(blank=True, default='', max_length=50, verbose_name='nick name')),
                ('is_featured', models.BooleanField(default=False, verbose_name='featured')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='birth date')),
                ('birth_place', models.CharField(blank=True, default='', max_length=200, verbose_name='birth place')),
                ('deathdate', models.DateField(blank=True, null=True, verbose_name='death date')),
                ('death_place', models.CharField(blank=True, default='', max_length=200, verbose_name='death place')),
                ('content', ckeditor.fields.RichTextField(blank=True, default='', verbose_name='biography')),
                ('content_source', models.URLField(blank=True, default='', verbose_name='content source')),
                ('trailer', models.URLField(blank=True, default='', help_text='trailer url (ONLY for youtube videos yet)', verbose_name='trailer')),
                ('trailer_info', models.CharField(blank=True, default='', max_length=250, verbose_name='trailer info')),
                ('image', models.ImageField(blank=True, null=True, upload_to=celebs.models.celeb_directory_path, verbose_name='image')),
                ('image_credit', models.CharField(blank=True, default='', max_length=250, verbose_name='image credit')),
            ],
            options={
                'verbose_name': 'celebrity',
                'verbose_name_plural': 'celebrities',
                'ordering': ('last_name', 'first_name'),
            },
        ),
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(editable=False, verbose_name='added date')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='updated date')),
                ('name', models.CharField(max_length=245, unique=True, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='slug')),
                ('code', models.CharField(db_index=True, max_length=1, verbose_name='code')),
                ('extra_chars_count', models.PositiveSmallIntegerField(default=0, editable=False, help_text='there is no need for extra chars for slug of this model             and if no need for it to be editable also.', verbose_name='extra characters count')),
            ],
            options={
                'verbose_name': 'duty',
                'verbose_name_plural': 'duties',
                'ordering': ('code',),
            },
        ),
    ]
