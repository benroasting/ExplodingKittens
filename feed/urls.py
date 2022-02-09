from django.urls import path
from .views import PostListView, PostDetailView, CreatePostView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('create_post', CreatePostView.as_view(), name='create_post'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_details')
]