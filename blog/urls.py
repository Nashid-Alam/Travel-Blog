from django.urls import include, path
from . import views


urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('discussion/', views.DiscussionList.as_view(), name='discussion_list'),
    path('discussion/<int:pk>', views.DiscussionDetail.as_view(), name='discussion_detail'),
    path('do/', views.DoList.as_view(), name='do_list'),
    path('do/<int:pk>', views.DoDetail.as_view(), name='do_detail'),
    path('place/', views.PlaceList.as_view(), name='Place_list'),
    path('place/<int:pk>', views.PlaceDetail.as_view(), name='Place_detail'),
    path('picture/', views.PictureList.as_view(), name='Picture_list'),
    path('picture/<int:pk>', views.PictureDetail.as_view(), name='Picture_detail'),

]
