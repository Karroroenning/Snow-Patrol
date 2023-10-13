from .models import BlogPost
from django import forms


class BlogPostForm(forms.ModelForm):
    """BlogPost form"""


class Meta:
    """meta class"""
    model = BlogPost
    fields = (
        'title',
        'author',
        'content',
        'featured_image',
    )
