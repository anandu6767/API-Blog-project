from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    BlogListView, BlogDetailView, BlogCreateView,
    BlogUpdateView, BlogDeleteView, CategoryViewSet
)

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blogs/create/', BlogCreateView.as_view(), name='blog-create'),
    path('blogs/<int:pk>/edit/', BlogUpdateView.as_view(), name='blog-edit'),
    path('blogs/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
]


urlpatterns += router.urls
