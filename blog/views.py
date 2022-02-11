from rest_framework import generics
from django.contrib.auth.models import User
from . import models
from .serializers import (
    CitySerializer,
    PostSerializer,
    PostDetailSerializer,
    DiscussionSerializer,
    DoSerializer,
    PictureSerializer,
    PlaceSerializer,
)


class PostList(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = PostDetailSerializer


class DiscussionList(generics.ListCreateAPIView):
    queryset = models.Discussion.objects.all()
    serializer_class = DiscussionSerializer

    def perform_create(self, serializer):
        owner = User.objects.get(pk=self.request.data.get("owner"))
        post = models.Post.objects.get(pk=self.request.data.get("post"))
        serializer.save(owner=owner, post=post)


class DiscussionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Discussion.objects.all()
    serializer_class = DiscussionSerializer


class DoList(generics.ListCreateAPIView):
    queryset = models.Do.objects.all()
    serializer_class = DoSerializer


class DoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Do.objects.all()
    serializer_class = DoSerializer


class PlaceList(generics.ListCreateAPIView):
    queryset = models.Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Place.objects.all()
    serializer_class = PlaceSerializer


class PictureList(generics.ListCreateAPIView):
    queryset = models.Picture.objects.all()
    serializer_class = PictureSerializer


class PictureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Picture.objects.all()
    serializer_class = PictureSerializer


class CityList(generics.ListCreateAPIView):
    queryset = models.City.objects.all()
    serializer_class = CitySerializer


class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.City.objects.all()
    serializer_class = CitySerializer
