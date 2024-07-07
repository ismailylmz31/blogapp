from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def blogs(request):
    return render(request, "blog/blogs.html")


def blog_details(request, slug):
    blog = blog.objects.get(slug=slug)
    return render(request,"blog/blog_details.html",
                  {"blog":blog})