from django.db.models import Q
from rest_framework import viewsets
from comments.models import Comment
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import CommentSerializer
from posts.api.pagination import PostCommentPagination


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PostCommentPagination
    search_fields = ['content', 'user__first_name']

    def get_queryset(self, *args, **kwargs):
        print('self.acton=', self.action)
        if self.action == 'list':
            queryset_list = Comment.objects.filter(approved=True, live=True,
                                                   post_id=self.kwargs['post'])
        else:
            queryset_list = Comment.objects.filter(approved=True, live=True)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list
