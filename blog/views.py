from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'santosh',
        'title': 'Title 1',
        'content': 'Python basic post1',
        'date_posted': '20-04-2020'
    },
    {
        'author': 'parul',
        'title': 'Title 2',
        'content': 'Python basic post2',
        'date_posted': '20-04-2020'
    }
]


# Create your views here.
def home(request):
    data = {'posts': posts}
    return render(request, 'blog/home.html', data)


def about(request):
    return HttpResponse('<h1> Blog About </h1>', {'title': 'About Us'})
