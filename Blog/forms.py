from django import forms
from tinymce.widgets import TinyMCE
from .models import Post, Comment

from django import forms




class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    overview = forms.CharField(widget=forms.Textarea(
        attrs={'class': "form-control",
               'rows': "3",
               }),
    )
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': True, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = ('title','overview', 'content', 'thumbnail', 
        'categories','featured', 'previous_post', 'next_post')


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        fields = ('comment', )