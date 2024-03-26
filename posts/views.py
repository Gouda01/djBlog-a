from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Post
from .forms import PostForm



# Create your views here.

def post_list(request):

    data = Post.objects.all()
    context = {
        'object_list' : data
    }
    return render(request,'posts/post_list.html', context)


def post_details(request,pk):
    data = Post.objects.get(id = pk)
    context = {
        'post' : data
    }

    return render(request,'posts/post_detail.html',context)



def create_post (request) :
    if request.method == 'POST' :
        form = PostForm(request.POST,request.FILES)
        if form.is_valid() :
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/posts/')
    else :
        form = PostForm()
    return render (request,'posts/new.html', {'form':form})




class PostList(ListView):
    model = Post


class PostDetail(DetailView):
    model = Post