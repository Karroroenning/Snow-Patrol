from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogPostForm


class BlogList(generic.ListView):
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blogpost.html'
    paginate_by = 6


class BlogDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = BlogPost.objects.filter(status=1)
        blogpost = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "blog/blogpost_detail.html",
            {
                "blogpost": blogpost,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = BlogPost.objects.filter(status=1)
        blogpost = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "blog/blogpost_detail.html",
            {
                "blogpost": blogpost,
            },
        )


class BlogLike(View):

    def post(self, request, slug):
        blogpost = get_object_or_404(Recipes, slug=slug)

        return HttpResponseRedirect(reverse('blogpost_detail', args=[slug]))
