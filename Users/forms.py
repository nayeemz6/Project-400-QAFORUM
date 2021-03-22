from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from mainapp.models import Question, Answer
from Users.models import Qauser



class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control",
               'id': "first_name",
               'type': "text"}),
        min_length=1,
        max_length=12,
        required=False
    )

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control",
               'id': "last_name",
               'type': "text"}),
        min_length=1,
        max_length=12,
        required=False
    )

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': "form-control",
               'id': "email",
               'type': "text"}),
        required=False
    )


    about_text = forms.CharField(widget=forms.Textarea(
        attrs={'class': "form-control",
               'id': "about_me",
               'rows': "4",
               }),
        max_length=500,
        required=False
    )

    facebook = forms.CharField(widget=forms.URLInput(
        attrs={'class': "form-control",
               'id': "facebook"}),
        required=False

    )

    website = forms.CharField(widget=forms.URLInput(
        attrs={'class': "form-control",
               'id': "homepage"}),
        required=False
    )

    github = forms.CharField(widget=forms.URLInput(
        attrs={'class': "form-control",
               'id': "github"}),
        required=False,
       
    )

    twitter = forms.CharField(widget=forms.URLInput(
        attrs={'class': "form-control",
               'id': "twitter"}),
        required=False,
        
    )

    class Meta:
        model = Qauser
        fields = ('first_name', 'last_name', 'email',
                  'profile_pic', 'about_text', 'facebook',
                  'website', 'github', 'twitter')


class QuestionForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control",
               'placeholder': "Question title"}),
        required=True, min_length=1, max_length=250)

    url = forms.URLField(widget=forms.URLInput(
        attrs={'class': "form-control",
               'placeholder': "(Optional) http:///www.example.com"}),
        required=False)

    detail = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': "form-control",
            'placeholder': "Type Your texts",
             'rows': '4'}),
        max_length=5000,
        required=False)

    tags = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control",
               'placeholder': "tags: ex.. programming"}),
        required=True, min_length=1, max_length=250)

    class Meta:
        model = Question
        fields = ('title', 'url', 'detail','tags')

class AnswerForm(ModelForm):
    detail = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': "form-control",
            'placeholder': "Type Your Answers here",
             'rows': '4'}),
        max_length=5000,
        required=False)
    class Meta:
        model=Answer
        fields=('detail',)