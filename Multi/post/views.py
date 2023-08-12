from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from .forms import PostForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


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
        started_at = request.POST['started_at']
        arrive_place = request.POST['arrive_place']
        post = Post(
            title=title,
            content=content,
            user=user,
            started_at=started_at,
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
    
def postUpdate(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST" and request.user.is_authenticated and request.user == post.user :
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.started_at = request.POST['started_at']
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
    User = get_user_model()
    # 팔로우 당하는 사람
    user = User.objects.get(pk=pk)
    if user != request.user:
        # 팔로우를 요청한 사람 => request.user
        # 팔로우가 되어 있다면,
        if user.followers.filter(pk=request.user.pk).exists():
            # 삭제
            user.followers.remove(request.user)
        else:
            # 추가
            user.followers.add(request.user)
        return render(request, 'post/post_detail.html')
    return redirect('/post')
