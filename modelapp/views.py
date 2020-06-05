from django.shortcuts import render
from .models import Blog

# Create your views here.
def home2(repuest):
    blog = Blog.objects
    return render(repuest,'home2.html', {'blog':blog})
