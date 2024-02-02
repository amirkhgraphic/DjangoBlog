from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.views.generic import FormView, ListView, DetailView
from apps.posts.forms import CreatePostForm
from apps.posts.models import Category, Post, Comment


@method_decorator(login_required, name='dispatch')
class CreatePost(FormView):
    form_class = CreatePostForm
    template_name = 'posts/create.html'
    success_url = reverse_lazy('posts:home')
    extra_context = {
        'title_of_template': 'Create Post',
    }

    def form_valid(self, form):
        category_name = form.cleaned_data.get('category_name')
        category, created = Category.objects.get_or_create(name=category_name)

        post = form.save(commit=False)
        post.author = self.request.user
        post.category = category
        post.save()

        if post is not None:
            return HttpResponseRedirect(self.success_url)

        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ListPosts(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'
    ordering = '-created_at'


@method_decorator(login_required, name='dispatch')
class DetailPost(DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@login_required()
@require_http_methods(["POST"])
def comment(request):
    body = request.POST['body']
    pk = request.POST['pk']
    if body:
        post = Post.objects.get(id=pk)
        Comment(post=post, user=request.user, body=body).save()
    return redirect(f'/posts/detail/{pk}')


@method_decorator(login_required, name='dispatch')
class CategoryListPosts(ListView):
    model = Post
    template_name = 'posts/category.html'
    context_object_name = 'posts'
    ordering = '-created_at'


@method_decorator(login_required, name='dispatch')
class AuthorListPosts(ListView):
    model = Post
    template_name = 'posts/author.html'
    context_object_name = 'posts'
    ordering = '-created_at'
