from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='Cat Name',
        widget=forms.Textarea(attrs={
            'rows': '1',
            'placeholder': 'What is the cats name?'
            })
    )
    body = forms.CharField(
        label='Cat Description',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Tell us about the cat...'
            }))

    image = forms.ImageField(required=False)        

    class Meta:
        model = Post
        fields = ['title', 'body', 'image']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '2',
            'placeholder': 'Make a comment about the cat...'
            }))

    class Meta:
        model = Comment
        fields = ['comment']