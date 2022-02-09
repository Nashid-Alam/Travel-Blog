from rest_framework import serializers
from .models import City, Discussion, Do, Picture, Place, Post


class PostSerializer(serializers.ModelSerializer):
    # city = serializers.ReadOnlyField(source='city.name')
    # country = serializers.ReadOnlyField(source='city.country')
    class Meta:
        model = Post
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    posts = PostSerializer(read_only=True, many=True)
    
    class Meta:
        model = City
        fields = ['id', 'name', 'country', 'posts']


class DiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion
        fields = '__all__'


class DoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Do
        fields = '__all__'


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
