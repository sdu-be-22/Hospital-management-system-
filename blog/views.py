from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from blog.models import Post, Category, Comment
from .forms import CommentForm
from django.urls import reverse, reverse_lazy

def candy(request):
  posts = Post.objects.all()[:5]
  cats = Category.objects.all()
  data = {
    'posts': posts,
    'cats': cats
  }
  return render(request, 'candy.html', data)

def post(request, pk):
  post = Post.objects.get(pk=pk)
  cats = Category.objects.all()

  if request.method == 'POST':
    form = CommentForm(request.POST)

    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = post
      comment.save()

      def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})
  else:
    form = CommentForm()
    
  return render(request, "posts.html", {'post': post, 'cats': cats, 'form': form})

def category(request, url):
  cat = Category.objects.get(url=url)
  posts = Post.objects.filter(cat=cat)
  
  return render(request, "category.html", {'cat': cat, 'posts': posts})