# forms.py

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post', 'image']
        widgets = {
            'post': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control1'}),
        }
        labels = {
            'post': 'Content:',
            'image': 'Post Image',
        }

class ReactionForm(forms.Form):
    # You can include fields here if necessary
    pass    


        