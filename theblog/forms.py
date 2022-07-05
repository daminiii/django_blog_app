from tkinter import Widget
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'title', 'title_tag', 'author', 'small_desc', 'full_desc')

        widget = {
            'image' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'small_desc': forms.Textarea(attrs={'class': 'form-control'}),
            'full_desc': forms.Textarea(attrs={'class': 'form-control'}),
        }