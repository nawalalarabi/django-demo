from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "Write your title"}),
            'content': forms.Textarea(attrs={'placeholder': "Write your post content"})
        }


class PostEdit(forms.Form):
    title = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={'placeholder': "Write your title"}),
        required=False
    )
    content = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': "Write your post content"}),
        required=False
    )
