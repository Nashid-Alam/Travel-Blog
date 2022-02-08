from django.urls import include, path
from . import views


urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('discussion/', views.DiscussionList.as_view(), name='discussion_list'),
    path('discussion/<int:pk>', views.DiscussionDetail.as_view(), name='discussion_detail')
]
