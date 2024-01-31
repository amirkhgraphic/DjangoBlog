from apps.posts.models import Post
from django import forms


class CreatePostForm(forms.ModelForm):
    category_name = forms.CharField(max_length=255, required=True)

    class Meta:
        model = Post
        fields = ('title', 'body')

