from rest_framework import generics, permissions, viewsets
from .models import Blog, Category
from .serializers import (
    BlogListSerializer,
    BlogDetailSerializer,
    CategorySerializer
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.select_related('category', 'author').all().order_by('-created_date')
    serializer_class = BlogListSerializer
    permission_classes = [IsAuthenticated]


class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.select_related('category', 'author').all()
    serializer_class = BlogDetailSerializer
    permission_classes = [IsAuthenticated]


class BlogCreateView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogUpdateView(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class BlogDeleteView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
