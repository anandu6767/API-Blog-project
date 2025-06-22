from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Blog
import re

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogListSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'created_date', 'category', 'author']

    def get_category(self, obj):
        return {
            'id': obj.category.id,
            'title': obj.category.title
        }

class BlogDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['author', 'created_date', 'modified_date']

    def validate_title(self, value):
        if not value or not re.search(r'[A-Za-z]', value):
            raise serializers.ValidationError("Title must contain at least one alphabetic character.")
        return value

    def validate(self, data):
        title = data.get('title', '')
        description = data.get('description', '')
        if title == description:
            raise serializers.ValidationError("Title and Description cannot be the same.")
        return data

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
