"""All model fields are put here for educational/experimental purpose"""

from django.db.models import Count

from rest_framework import serializers

from celebs.models import Celebrity, Duty


class CelebritySerializer(serializers.HyperlinkedModelSerializer):
    duties = serializers.HyperlinkedRelatedField(
        view_name='celebs:duty-detail', lookup_field='slug',
        many=True, read_only=True
    )

    class Meta:
        model = Celebrity
        fields = (
            'url', 'id',
            'name', 'slug', 'first_name', 'last_name', 'nick_name',
            'is_featured',
            'birthdate', 'birth_place', 'deathdate', 'death_place',
            'content', 'content_source', 'trailer', 'trailer_info',
            'image', 'image_credit',
            'duties',
            'added_at')
        # 'added_at', 'added_by', 'updated_at', 'updated_by'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {
                'view_name': 'celebs:celeb-detail',
                'lookup_field': 'slug'}
        }


class DutySerializer(serializers.HyperlinkedModelSerializer):
    celebs = serializers.HyperlinkedRelatedField(
        view_name='celebs:celebrity-detail', lookup_field='slug',
        many=True, read_only=True
    )
    celebs_count = serializers.ReadOnlyField(source='celebs.count')

    class Meta:
        model = Duty
        fields = (
            'url', 'id',
            'name', 'slug', 'code', 'celebs_count',
            'celebs')
        # 'added_at', 'added_by', 'updated_at', 'updated_by'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {
                'view_name': 'celebs:duty-detail',
                'lookup_field': 'slug'}
        }
