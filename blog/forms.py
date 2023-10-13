from .models import BlogPost
from django import forms


class BlogPostForm(forms.ModelForm):
    """BlogPost form"""
    # Sets a required field on a Django model form.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True

    class Meta:
        """meta class"""
        model = BlogPost
        fields = (
            'title',
            'content',
        )

        labels = {
            'title': 'Blog Title',
            'content': 'Write your blog here',
        }