from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """Form for posting blogs"""

    class Meta:

        model = Post
        fields = ('title', 'text')


class CommentForm(forms.ModelForm):
    class Meta:

        model = Comment
        fields = ('text',)
