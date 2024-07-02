from django.shortcuts import render, get_object_or_404,redirect
from .models import Post, Comment
from .forms import PostForm
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

from django.http import JsonResponse

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
    is_liked= False
    post =  get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        is_liked =True
    context = {"post" : post, "is_liked" : is_liked}
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
            # tag 저장
            form.save_m2m()

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

def comment_create(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method =="POST":
        content = request.POST.get("content").strip()
        Comment.objects.create(user=request.user, post=post, content=content)
        # comment = Comment(user=request.user, post=post, content=content)
        # comment.save()

        return redirect("blog:detail", post_id)

    return redirect("blog:detail", post_id)

def post_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
   
    is_liked = post.likes.filter(id=request.user.id).exists()
   
    is_liked_change = False

    if is_liked:
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        is_liked_change = True

    return JsonResponse({"like": post.likes.count() , "is_liked":is_liked_change})
    
        
    
        


    