"""all model fields are put here for educational/experimental purpose"""

from rest_framework import serializers

from movies.models import Genre, Movie, PgRating


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = (
            'url', 'id',
            'name', 'slug', 'code', 'content',
            'added_at', 'added_by', 'updated_at', 'updated_by')


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'url', 'id',
            'name', 'slug', 'name', 'original_name',
            'is_featured',
            'release_year', 'duration', 'imdb_rating',
            'content', 'content_source', 'trailer', 'trailer_info',
            'image', 'image_credit',
            'age', 'trailer_video', 'duration_humanize',
            'pg_rating', 'genres', 'crews',
            'added_at', 'added_by', 'updated_at', 'updated_by')


class PgRatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PgRating
        fields = (
            'url', 'id',
            'name', 'slug', 'code', 'content',
            'added_at', 'added_by', 'updated_at', 'updated_by')
