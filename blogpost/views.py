from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from blogpost.models import Post
from blogpost.forms import PostForm
from django.urls import reverse_lazy


# Create your views here.
# def home(request):
#     return render(request,"home.html",{})

class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering=['-id']


class ArticleDetail(DetailView):
    model = Post
    template_name = "article_detail.html"


class AddPostView(CreateView):
    model = Post
    form_class= PostForm
    template_name = "add_post.html"
    
    # fields="__all__"  

class UpdatePostView(UpdateView):
    model = Post
    template_name = "update_post.html"
    fields=['author','title','body'] 


class DeletePostView(DeleteView):
    model = Post
    template_name = "Delete_post.html"
    success_url= reverse_lazy('home')

