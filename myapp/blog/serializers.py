from rest_framework import serializers
from . models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("user", "created_at", "slug")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
