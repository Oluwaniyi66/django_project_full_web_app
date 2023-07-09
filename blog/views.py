from django.shortcuts import render
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


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
