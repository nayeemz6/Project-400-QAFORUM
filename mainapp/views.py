from django.shortcuts import render, HttpResponse,redirect, reverse
from django.http import JsonResponse
from .models import Question, Answer, Comment, UpVote, DownVote
from django.core.paginator import Paginator
from django.contrib import messages
from Users.forms import AnswerForm, QuestionForm, ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Users.models import Qauser
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
# Home Page


def home(request):
    latest = Question.objects.all().order_by("-id")
    quests = Question.objects.all()
    tags = []
    for quest in quests:
        qtags = [tag.strip() for tag in quest.tags.split(',')]
        for tag in qtags:
            if tag not in tags:
                tags.append(tag)
    # Fetch Questions
    tag_with_count = []
    for tag in tags:
        tag_data = {
            'name': tag,
            'count': Question.objects.filter(tags__icontains=tag).count()
        }
        tag_with_count.append(tag_data)
    if 'q' in request.GET:
        q = request.GET['q']
        quests = Question.objects.annotate(total_comments=Count(
            'answer__comment')).filter(title__icontains=q).order_by('-id')
    else:
        quests = Question.objects.annotate(
            total_comments=Count('answer__comment')).all().order_by('-id')
    paginator = Paginator(quests, 3)
    page_num = request.GET.get('page', 1)
    quests = paginator.page(page_num)

    return render(request, 'home.html', {'quests': quests, 'tags': tags, 'tags': tag_with_count, 'latest':latest})

# Detail


def detail(request, id):
    latest = Question.objects.all().order_by("-id")
    quests = Question.objects.all()
    tags = []
    for quest in quests:
        qtags = [tag.strip() for tag in quest.tags.split(',')]
        for tag in qtags:
            if tag not in tags:
                tags.append(tag)
    # Fetch Questions
    tag_with_count=[]
    for tag in tags:
        tag_data={
            'name':tag,
            'count':Question.objects.filter(tags__icontains=tag).count()
        }
        tag_with_count.append(tag_data)

    quest=Question.objects.get(pk=id)
    tags=quest.tags.split(',')
    answers=Answer.objects.filter(question=quest)
    answerform=AnswerForm
    if request.method=='POST':
        answerData=AnswerForm(request.POST)
        if answerData.is_valid():
            answer=answerData.save(commit=False)
            answer.question=quest
            user = User.objects.get(username=request.user)
            answer.user=request.user.qauser
            answer.author = user
            answer.author_name = user.username
            answer.save()
            messages.success(request,'Answer has been submitted.')
    return render(request,'detail.html',{
        'quest':quest,
        'tags':tags,
        'tags':tag_with_count,
        'answers':answers,
        'answerform':answerform,
        'latest':latest
    })

# Save Comment
@login_required
def save_comment(request):
    if request.method=='POST':
       
        comment=request.POST['comment']
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user.qauser
        Comment.objects.create(
            answer=answer,
            comment=comment,
            user=user
        )
        return JsonResponse({'bool':True})

# Save Upvote
def save_upvote(request):
    if request.method=='POST':
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user.qauser
        check=UpVote.objects.filter(answer=answer,user=user).count()
        if check > 0:
            return JsonResponse({'bool':False})
        else:
            UpVote.objects.create(
                answer=answer,
                user=user
            )
            return JsonResponse({'bool':True})

# Save Downvote
def save_downvote(request):
    if request.method=='POST':
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user.qauser
        check=DownVote.objects.filter(answer=answer,user=user).count()
        if check > 0:
            return JsonResponse({'bool':False})
        else:
            DownVote.objects.create(
                answer=answer,
                user=user
            )
            return JsonResponse({'bool':True})


# Ask Form
@login_required
def ask_form(request):
    
    form=QuestionForm
    if request.method=='POST':
        questForm=QuestionForm(request.POST)
        if questForm.is_valid():
            questForm=questForm.save(commit=False)
            user = User.objects.get(username=request.user)
            questForm.user=request.user.qauser
            questForm.author = user
            questForm.author_name = user.username
            questForm.save()
            messages.success(request,'Question has been added.')
    return render(request,'ask-question.html',{'form':form})


# Questions according to tag
def tag(request,tag):
    latest = Question.objects.all().order_by("-id")
    quests=Question.objects.annotate(total_comments=Count('answer__comment')).filter(tags__icontains=tag).order_by('-id')
    paginator=Paginator(quests,10)
    page_num=request.GET.get('page',1)
    quests=paginator.page(page_num)
    return render(request,'tag.html',{'quests':quests,'tag':tag,'latest':latest})



# Tags Page
def tags(request):
    latest = Question.objects.all().order_by("-id")
    quests=Question.objects.all()
    tags=[]
    for quest in quests:
        qtags=[tag.strip() for tag in quest.tags.split(',')]
        for tag in qtags:
            if tag not in tags:
                tags.append(tag)
    # Fetch Questions
    tag_with_count=[]
    for tag in tags:
        tag_data={
            'name':tag,
            'count':Question.objects.filter(tags__icontains=tag).count()
        }
        tag_with_count.append(tag_data)
    return render(request,'tags.html',{'tags':tag_with_count,'tags':tags,'latest':latest})


class QuestUpdateView(UpdateView):
    model = Question
    template_name = 'ask-question.html'
    form_class = QuestionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user.qauser
        form.save()
        return redirect(reverse("detail", kwargs={
            'id': form.instance.pk
        }))

def quest_update(request, id):
    title = 'Update'
    quest = get_object_or_404(Question, id=id)
    form = questForm(
        request.POST or None,
        request.FILES or None,
        instance=post)
    author_name = request.user.qauser
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = author_name
            form.save()
            return redirect(reverse("detail", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, "ask-question.html", context)


class QuestDeleteView(DeleteView):
    model = Question
    success_url = '/'
    template_name = 'quest_confirm_delete.html'


def quest_delete(request, id):
    quest = get_object_or_404(Question, id=id)
    quest.delete()
    return redirect(reverse("blog/dashboard.html"))
        
        
