from re import T
from rest_framework import serializers
from .models import City, Discussion, Do, Picture, Place, Post


class DiscussionSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Discussion
        fields = ["id", "title", "content", "author"]


class DoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Do
        fields = "__all__"


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = "__all__"


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostDetailSerializer(serializers.ModelSerializer):
    city = serializers.ReadOnlyField(source="city.name")
    country = serializers.ReadOnlyField(source="city.country")
    discussions = DiscussionSerializer(read_only=True, many=True)
    pictures = PictureSerializer(read_only=True, many=True)
    places = PlaceSerializer(read_only=True,many=True)

    class Meta:
        model = Post
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    posts = PostSerializer(read_only=True, many=True)

    class Meta:
        model = City
        fields = ["id", "name", "country", "posts"]
