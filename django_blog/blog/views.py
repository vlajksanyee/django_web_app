from django.shortcuts import render

posts = [
    {
        'author': 'AlexB',
        'title': 'Blog Post #1',
        'content': 'This is my first post!',
        'date_posted': 'March 14, 2025'
    },
    {
        'author': 'DianaB',
        'title': 'Blog Post #2',
        'content': 'This is Diana\'s first post!',
        'date_posted': 'March 14, 2025'
    }
]

def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)
