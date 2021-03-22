from django.urls import path
from . import views
from .views import adminView,answer_delete,quest_delete, adminblogView,post_delete,comment_delete,adminusersView,user_delete
from Blog.views import PostUpdateView
urlpatterns=[
    path('qaadmin', adminView, name='qaadmin'),
    path('admin_blog', adminblogView, name='admin_blog'),
    path('admin_Users', adminusersView, name='admin_Users'),
    path('answer/<id>/delete', answer_delete, name='answer-delete'),
    path('quest/<id>/delete', quest_delete, name='quest-delete'),
    path('post/<id>/delete', post_delete, name='post-delete'),
    path('comment/<id>/delete', comment_delete, name='comment-delete'),
    path('post/<pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('user/<id>/delete', user_delete, name='user-delete'),
    
]   