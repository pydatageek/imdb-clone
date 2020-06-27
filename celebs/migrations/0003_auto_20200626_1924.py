# Generated by Django 3.0.7 on 2020-06-26 19:24

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celebs', '0002_auto_20200626_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='celebrity',
            name='first_name_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AddField(
            model_name='celebrity',
            name='last_name_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AddField(
            model_name='celebrity',
            name='name_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AddField(
            model_name='duty',
            name='name_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AddIndex(
            model_name='celebrity',
            index=django.contrib.postgres.indexes.GinIndex(fields=['first_name_vector', 'last_name_vector'], name='celebs_cele_first_n_c45950_gin'),
        ),
    ]
