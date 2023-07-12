from typing import Optional
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# posts = [
#     {
#         'author': 'ropo',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'July 05, 2023'
#     },
#     {
#         'author': 'folakemi',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'July 06, 2023'
#     },
#     {
#         'author': 'Love Doctor',
#         'title': 'Blog Post 3',
#         'content': 'Third post content',
#         'date_posted': 'July 07, 2023'
#     },
#     {
#         'author': 'Sexual Puritan',
#         'title': 'Blog Post 4',
#         'content': 'Fourth post content',
#         'date_posted': 'July 08, 2023'
#     },

# ]

# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # for backwards compatibility <app> /<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [ 'title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        model = Post
        fields = ['title', 'content']
        
        def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)
        
        #prevent any user from updating others posts
        def test_func(self):
            post = self.get_object()
            if self.request.user == post.author:
             return True
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Post
        success_url = '/'
        
        def test_func(self):
            post = self.get_object()
            if self.request.user == post.author:
                return True
            return False   
            
            
def about(request):
     return render(request, 'blog/about.html', {'title':'About'})
