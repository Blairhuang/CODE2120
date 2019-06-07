from django.shortcuts import render
from django.http improt HttpResponse

def home(request):
    return render(request,'blog/home.html') #Passing info to template

def about(request):
    return HttpResponse('<h1>Blog About</h1>')

### blog -> template -> blog1 -> template.html (路径)


# Create your views here.
# Change the name from 'wombat' into 'blog'
