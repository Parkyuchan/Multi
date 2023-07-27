from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from .forms import PostForm

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