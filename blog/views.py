from django.shortcuts import render

posts = [
    {
        'title': 'My First Blog 1',
        'author': 'Wasim Akram',
        'content': 'This is my first blog',
        'date_posted': '10th August 2025'
    },
    {
        'title': 'My First Blog 2',
        'author': 'Wasim Akram',
        'content': 'This is my Second blog',
        'date_posted': '11th August 2025'
    }    
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html', {'title':'about'})
