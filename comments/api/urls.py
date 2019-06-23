from django.urls import path

from .views import CommentViewSet

urlpatterns = [
    path('<int:post>/', CommentViewSet.as_view({'get': 'list'}), name='comment-list'),
    path('detail/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve',
                                                     'delete': 'destroy'}), name='comment-detail'),
    path('', CommentViewSet.as_view({'post': 'create'}), name='comment-create'),
]
