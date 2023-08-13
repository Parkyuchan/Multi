from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post
from django.core.exceptions import PermissionDenied
from .forms import PostForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post
def createPost(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        user = request.user
        started_date = request.POST['started_date']
        started_time = request.POST['started_time']
        arrive_place = request.POST['arrive_place']
        post = Post(
            title=title,
            content=content,
            user=user,
            started_date=started_date,
            started_time=started_time,
            arrive_place=arrive_place
        )
        post.save()
        return redirect('/post/')
    else:
        postForm = PostForm
        post = Post.objects.all()
        context = {
            'postForm': postForm,
            'post': post
        }
        return render(request, 'post/post_form.html', context)

class PostSearch(PostList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        post_list = Post.objects.filter(
            Q(title__contains=q)
        ).distinct()
        return post_list

    def get_context_data(self, **kwargs):
        context = super(PostSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'

        return context
    
def postUpdate(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST" and request.user.is_authenticated and request.user == post.user :
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.started_date = request.POST['started_date']
        post.started_time = request.POST['started_time']
        post.arrive_place = request.POST['arrive_place']
        post.save()
        return redirect('/post/')

    else:
        postForm = PostForm(instance=post)
        return render(request, 'post/post_update.html', {'postForm':postForm})
        
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user.is_authenticated and request.user == post.user:
        post.delete()
        return redirect('/post')
    else:
        raise PermissionDenied
    
@login_required
def follow(request, post_pk, user_pk):  
    post = Post.objects.get(id=post_pk)
    User = get_user_model()
    user = get_object_or_404(User, pk=user_pk)
    # 팔로우 당하는 사람
    
    if user != request.user:
        # 팔로우를 요청한 사람 => request.user
        # 팔로우가 되어 있다면,
        if post.followings.filter(pk=request.user.pk).exists():
            # 삭제
            post.followings.remove(request.user)
        else:
            # 추가
            post.followings.add(request.user)
        return redirect('/post/')
    return redirect('/post/')


def ending(request, pk):
    post = Post.objects.get(id=pk)
    post.ending = True
    
    post.save()
    return redirect('/post/')

def mypost(request, pk):
    post = Post.objects.all()
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    context = {
            'post': post,
            'user': user
        }
    
    return render(request, 'post/mypost.html', context)