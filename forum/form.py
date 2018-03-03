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