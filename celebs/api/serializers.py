"""all model fields are put here for educational/experimental purpose"""

from rest_framework import serializers

from celebs.models import Celebrity, Duty


class DutySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Duty
        fields = (
            'url', 'id',
            'name', 'slug', 'code',
            'added_at', 'added_by', 'updated_at', 'updated_by')


class CelebritySerializer(serializers.HyperlinkedModelSerializer):
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
            'added_at', 'added_by', 'updated_at', 'updated_by')
