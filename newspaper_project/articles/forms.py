from django import forms

from .models import Comment


class CommentCreateForm(forms.ModelForm):
    comment = forms.CharField(max_length=140)

    class Meta:
        model = Comment
        fields = ("comment",)
