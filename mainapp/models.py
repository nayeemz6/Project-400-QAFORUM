import mistune
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from Users.models import Qauser
from django.utils import timezone

   
    
class Question(models.Model):
    author_name = models.CharField(null=False, max_length=12)
    user = models.ForeignKey(Qauser,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    url = models.URLField(null=True, blank=True)
    detail = models.TextField(max_length=5000, blank=True)
    text_html = models.TextField(blank=True)
    tags = models.TextField(default='')
    add_time = models.DateTimeField(auto_now_add=True)

    def generate_html(self):
        if self.detail:
            html = mistune.markdown(self.detail)
            self.text_html = html

    def __str__(self):
        return self.title



# Answer Model
class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    user=models.ForeignKey(Qauser,on_delete=models.CASCADE)
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail

# Comment
class Comment(models.Model):
    author_name = models.CharField(null=False, max_length=12)
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    user=models.ForeignKey(Qauser,on_delete=models.CASCADE,related_name='comment_user')
    comment=models.TextField(default='')
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

# UpVotes
class UpVote(models.Model):
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    user=models.ForeignKey(Qauser,on_delete=models.CASCADE,related_name='upvote_user')

# DownVotes
class DownVote(models.Model):
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    user=models.ForeignKey(Qauser,on_delete=models.CASCADE,related_name='downvote_user')

