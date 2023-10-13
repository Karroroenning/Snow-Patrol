from django.db import models

from django.contrib.auth.models import User
from django.utils.text import slugify


STATUS = ((0, "Draft"), (1, "Published"))


class BlogPost(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blogpost"
    )
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(null=True, blank=True, default='placeholder')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
