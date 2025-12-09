from . import views
from .views import PostListView, PostDetailView
from django.urls import path

urlpatterns=[
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
]