from django.urls import path
from . import views
from .views import QuestUpdateView,QuestDeleteView
urlpatterns=[
    path('',views.home,name='home'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('save-comment',views.save_comment,name='save-comment'),
    path('save-upvote',views.save_upvote,name='save-upvote'),
    path('save-downvote',views.save_downvote,name='save-downvote'),
    # Ask QUestion
    path('ask-question',views.ask_form,name='ask-question'),
    # Tag Page
    path('tag/<str:tag>',views.tag,name='tag'),
    # Tags Page
    path('tags',views.tags,name='tags'),
    path('quest/<pk>/update/', QuestUpdateView.as_view(), name='quest-update'),
    path('quest/<pk>/delete/', QuestDeleteView.as_view(), name='quest-delete'),
]   