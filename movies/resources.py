from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

from celebs.models import Duty, Celebrity
from .models import Genre, PgRating, Movie, MovieCrew


class GenreResource(resources.ModelResource):
    class Meta:
        model = Genre


class PgRatingResource(resources.ModelResource):
    class Meta:
        model = PgRating


class MovieResource(resources.ModelResource):
    pg_rating = fields.Field(
        attribute='pg_rating',
        column_name='pg_rating',
        widget=ForeignKeyWidget(PgRating, field='code'))
    genres = fields.Field(
        attribute='genres',
        column_name='genres',
        widget=ManyToManyWidget(Genre, field='code', separator=','))

    class Meta:
        model = Movie


class MovieCrewResource(resources.ModelResource):
    """TODO: Code should be improved considering the performance"""
    duty = fields.Field(
        attribute='duty',
        column_name='duty',
        widget=ForeignKeyWidget(Duty, field='code'))
    movie = fields.Field(
        attribute='movie',
        column_name='movie',
        widget=ForeignKeyWidget(Movie, field='name'))
    crew = fields.Field(
        attribute='crew',
        column_name='crew',
        widget=ForeignKeyWidget(Celebrity, field='name'))

    class Meta:
        model = MovieCrew
