from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostList, PostDetail, AuthorViewSet

router = DefaultRouter()
# router.register(r'posts/$', PostList, basename='post_list')
# router.register(r'posts/$', PostDetail, basename='post_detail')
router.register(r'authors', AuthorViewSet, basename='author')
urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view())
]
urlpatterns += router.urls