from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (TagView, CommentView, TopBlogView, BlogView, ImageView, SpecialblogView)


router = DefaultRouter()
router.register('tag-url', TagView, basename='tag-url')
router.register('comment-url', CommentView, basename='comment-url')
router.register('top-blog-url', TopBlogView, basename='top-blog-url_list')
router.register('blog-url', BlogView, basename='blog-url')
router.register('image-url', ImageView, basename='image-url')
router.register('specialblog-url', SpecialblogView, basename='specialblog-url_list')

urlpatterns = [
	path('', include(router.urls)),
]
