from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .pagination import PostCommentPagination
from posts.models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.decorators import action


class BlogPostViewSet(viewsets.ModelViewSet):
    serializer_class = BlogPostSerializer
    pagination_class = PostCommentPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = BlogPost.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
        return qs

    # @action(detail=True, methods=['post'])
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
