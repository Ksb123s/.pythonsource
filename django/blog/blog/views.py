from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

# Create your views here.
def list(request):

    page =request.GET.get('page', 1)

    # 전체 포스트 조회
    post_list = Post.objects.all()

    paginator = Paginator(post_list, 5)
    page_ob = paginator.get_page(page)
    context = {"post_list" : page_ob}
    return render(request, "blog/list.html", context)

def detail(request, post_id):

    post =  get_object_or_404(Post, id=post_id)
    context = {"post" : post}
    return render(request, "blog/post.html", context)

@login_required(login_url="common:login")
def create(request):
    if request.method =="POST":
        #  폼에 post 로 넘어오는 내용 담기
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
           post= form.save(commit=False)
           post.user = request.user
           post.save()
           return redirect("blog:list")
        #    return redirect("blog:detail", post.id)
    else:
        form = PostForm()
        
    return render(request, "blog/create.html", {"form":form})


def modify(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method =="POST":
        #  폼에 post 로 넘어오는 내용 담기
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post= form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("blog:detail", post.id)
    else:
        form = PostForm(instance=post)
        
    return render(request, "blog/modify.html", {"form":form, "post":post})

def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    post.delete()

    return redirect("blog:list")