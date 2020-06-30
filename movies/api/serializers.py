"""All model fields are put here for educational/experimental purpose"""

from rest_framework import serializers

from movies.models import Genre, Movie, PgRating


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    movies = serializers.HyperlinkedRelatedField(
        view_name='movies:movie-detail', lookup_field='slug',
        many=True, read_only=True
    )
    movies_count = serializers.ReadOnlyField(source='movies.count')

    class Meta:
        model = Genre
        fields = (
            'url', 'id',
            'name', 'slug', 'code', 'content', 'movies_count', 'movies')
        # 'added_at', 'added_by', 'updated_at', 'updated_by'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {
                'view_name': 'movies:genre-detail',
                'lookup_field': 'slug'}
        }


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    pg_rating = serializers.HyperlinkedRelatedField(
        view_name='movies:pgrating-detail', lookup_field='slug',
        many=False, read_only=True
    )
    genres = serializers.HyperlinkedRelatedField(
        view_name='movies:genre-detail', lookup_field='slug',
        many=True, read_only=True
    )
    crews = serializers.HyperlinkedRelatedField(
        view_name='celebs:celebrity-detail', lookup_field='slug',
        many=True, read_only=True
    )

    class Meta:
        model = Movie
        fields = (
            'url', 'id',
            'name', 'slug', 'name', 'original_name',
            'is_featured',
            'release_date', 'duration', 'imdb_rating',
            'content', 'content_source', 'trailer', 'trailer_info',
            'image', 'image_credit',
            'age', 'trailer_video', 'duration_humanize',
            'pg_rating', 'genres', 'crews',
            'added_at')
        # 'added_at', 'added_by', 'updated_at', 'updated_by'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {
                'view_name': 'movies:movie-detail',
                'lookup_field': 'slug'}
        }


class PgRatingSerializer(serializers.HyperlinkedModelSerializer):
    movies = serializers.HyperlinkedRelatedField(
        view_name='movies:movie-detail', lookup_field='slug',
        many=True, read_only=True
    )
    movies_count = serializers.ReadOnlyField(source='movies.count')

    class Meta:
        model = PgRating
        fields = (
            'url', 'id',
            'name', 'slug', 'code', 'content', 'movies_count', 'movies')
        # 'added_at', 'added_by', 'updated_at', 'updated_by'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {
                'view_name': 'movies:pgrating-detail',
                'lookup_field': 'slug'}
        }
