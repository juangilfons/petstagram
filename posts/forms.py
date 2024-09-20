from django import forms

from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']
        labels = {
            'image': 'Drag and drop or click to select an image',
            'caption': 'Caption',
        }
        widgets = {
            ''
        }
