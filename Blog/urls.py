from django.urls import path
from django.conf.urls import url
from .views import (
    search,
    post_list,
    post_detail,
    post_create,
    post_update,
    post_delete,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    dashboard
)
urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog'),
    path('search/', search, name='search'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('dashboard/',dashboard, name='dashboard'),
]