
from django.shortcuts import render, redirect,reverse
from mainapp.models import Question, Answer, Comment, UpVote, DownVote
from Blog.models import PostView, Post, Comment
from Users.models import Qauser
from django.contrib.auth.decorators import login_required
from Users.decorators import *
from django.db.models import Count
from django.shortcuts import get_list_or_404, get_object_or_404
# Create your views here.


@login_required
@allowed_users(allowed_roles=['Admin'])
def adminView(request):

    quest = Question.objects.all()
    quest = Question.objects.annotate(
            total_comments=Count('answer__comment')).all().order_by('-id')

    answer = Answer.objects.all()
    total_ans = answer.count()
    comment = Comment.objects.all()
    total_ans = comment.count()
    up = UpVote.objects.all()
    total_up = up.count()
    down = DownVote.objects.all()
    total_down = down.count()
    context = {
        'answer': answer,
        'quest': quest,
        'comment': comment,
        'up':up,
        'down':down,
    }
    return render(request, 'admin_dashboard.html', context)


@login_required
@allowed_users(allowed_roles=['Admin'])
def answer_delete(request, id):
    
    answer = get_object_or_404(Answer, pk=id)
    answer.delete()
    return redirect(reverse("qaadmin"))

@login_required
@allowed_users(allowed_roles=['Admin'])
def quest_delete(request, id):
    
    quest = get_object_or_404(Question, pk=id)
    quest.delete()
    return redirect(reverse("qaadmin"))

@login_required
@allowed_users(allowed_roles=['Admin'])
def adminblogView(request):

    post = Post.objects.all()
    total_post = post.count()

    postview = PostView.objects.all()
    total_view = postview.count()
    comment = Comment.objects.all()
    total_comment = comment.count()
    context = {
        'post': post,
        'postview': postview,
        'comment': comment,
    }
    return render(request, 'admin_blog.html', context)


@login_required
@allowed_users(allowed_roles=['Admin'])
def comment_delete(request, id):
    
    comment = get_object_or_404(Comment, pk=id)
    comment.delete()
    return redirect(reverse("admin_blog"))

@login_required
@allowed_users(allowed_roles=['Admin'])
def post_delete(request, id):
    
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect(reverse("admin_blog"))

@login_required
@allowed_users(allowed_roles=['Admin'])
def adminusersView(request):
    user = Qauser.objects.all()
    total_user= user.count()
    context = {
    'user': user,
    
    }
    return render(request, 'admin_Users.html', context)

@login_required
@allowed_users(allowed_roles=['Admin'])
def user_delete(request, id):
    
    user = get_object_or_404(Qauser, pk=id)
    user.delete()
    return redirect(reverse("admin_Users"))

