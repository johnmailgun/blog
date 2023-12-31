from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy

from .models import Post
# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

class BlogListView(ListView):
    model = Post
    context_object_name = "wholemodel"

class BlogDetailView(DetailView):
    model = Post

class BlogCreateView(CreateView):
    model = Post
    fields = ['head','text']

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['head','text']

class BlogDeleteView(DeleteView):
    model = Post
    fields = ['head','text']
    success_url = reverse_lazy('index')

