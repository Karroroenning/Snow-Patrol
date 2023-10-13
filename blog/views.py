from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogPostForm


class BlogList(generic.ListView):
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blogpost.html'
    paginate_by = 9


class BlogDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = BlogPost.objects.filter(status=1)
        blogpost = get_object_or_404(queryset, slug=slug)
        liked = False
        if blogpost.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog_detail.html",
            {
                "blogpost": blogpost,
                "liked": liked,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = BlogPost.objects.filter(status=1)
        blogpost = get_object_or_404(queryset, slug=slug)
        liked = False
        if blogpost.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog_detail.html",
            {
                "blogpost": blogpost,
                "liked": liked,
            },
        )


class BlogLike(View):

    def post(self, request, slug):
        blogpost = get_object_or_404(Recipes, slug=slug)

        if blogpost.likes.filter(id=request.user.id).exists():
            blogpost.likes.remove(request.user)
        else:
            blogpost.likes.add(request.user)

        return HttpResponseRedirect(reverse('blog_detail', args=[slug]))


@login_required()
def add_blogpost(request):
    """renders add BlogPost form"""
    submitted = False
    if request.method == "POST":
        blogpost_form = BlogPostForm(request.POST, request.FILES)
        if blogpost_form.is_valid():
            blogpost_form.instance.creator = request.user
            blogpost_form.save()
            messages.add_message
            (request, messages.SUCCESS, 'Your blogpost is awaiting approval.')
            return redirect('blogpost')
    else:
        blogpost_form = BlogPostForm
        if 'submitted' in request.GET:
            submitted = True
    return render(
        request,
        'add_blogpost.html',
        {'blogpost_form': blogpost_form, 'submitted': submitted})


@login_required()
def edit_blogpost(request, slug):
    """BlogPost update/edit view"""
    blogpost = get_object_or_404(BlogPost, slug=slug)
    blogpost_form = BlogPostForm(request.POST or None, instance=blogpost)
    context = {
        "blogpost_form": blogpost_form,
        "blogpost": blogpost,
    }
    if request.method == "POST":
        blogpost_form = BlogPostForm(request.POST, request.FILES,
                                     instance=blogpost)
        if blogpost_form.is_valid():
            blogpost = blogpost_form.save(commit=False)
            blogpost.creator = request.user
            blogpost.save()
            messages.add_message(request, messages.SUCCESS, 'BlogPost updated!')
            return redirect('blogpost')
    else:
        blogpost_form = BlogPostForm(instance=blogpost)
    return render(request, "edit_blogpost.html", context)


@login_required()
def delete_blogpost(request, slug):
    """Delete blogpost"""
    blogpost = get_object_or_404(BlogPost, slug=slug)
    blogpost.delete()
    messages.add_message(request, messages.SUCCESS, 'BlogPost deleted.')
    return redirect('blogpost')
