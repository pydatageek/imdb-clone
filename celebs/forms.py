from django import forms

# from reviews.models import CelebComment
from .models import Celebrity


class CelebrityForm(forms.ModelForm):
    class Meta:
        model = Celebrity
        fields = '__all__'
        widgets = {
            'duties': forms.CheckboxSelectMultiple
        }


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = CelebComment
#         fields = ('text', 'celeb')
#         widgets = {
#             'text': forms.Textarea(attrs={'rows': 5}),
#             'celeb': forms.HiddenInput,
#         }
