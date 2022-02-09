from django.urls import include, path
from . import views


urlpatterns = [
    path("posts/", views.PostList.as_view(), name="post_list"),
    path("posts/<int:pk>", views.PostDetail.as_view(), name="post_detail"),
    path("discussions/", views.DiscussionList.as_view(), name="discussion_list"),
    path(
        "discussions/<int:pk>",
        views.DiscussionDetail.as_view(),
        name="discussion_detail",
    ),
    path("dos/", views.DoList.as_view(), name="do_list"),
    path("dos/<int:pk>", views.DoDetail.as_view(), name="do_detail"),
    path("places/", views.PlaceList.as_view(), name="place_list"),
    path("places/<int:pk>", views.PlaceDetail.as_view(), name="place_detail"),
    path("pictures/", views.PictureList.as_view(), name="picture_list"),
    path("pictures/<int:pk>", views.PictureDetail.as_view(), name="picture_detail"),
    path("cities/", views.CityList.as_view(), name="city_list"),
    path("cities/<int:pk>", views.CityDetail.as_view(), name="city_detail"),
]
