from django import forms

from .models import Genre, PgRating


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name', 'slug', 'code', 'content')
        widgets = {
            'content': forms.Textarea({'rows': 3})
        }


class PgRatingForm(forms.ModelForm):
    class Meta:
        model = PgRating
        fields = ('name', 'slug', 'code', 'content')
        widgets = {
            'content': forms.Textarea({'rows': 3})
        }


"""
from reviews.models import MovieComment
class CommentForm(forms.ModelForm):
    class Meta:
        model = MovieComment
        fields = ('text', 'movie')
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5}),
            'movie': forms.HiddenInput,
        }
"""
