from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': posts})
