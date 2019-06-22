from django.conf.urls import url

from .views import CommentViewSet

urlpatterns = [
    url(r'^(?P<post>\w+)/$', CommentViewSet.as_view({'get': 'list'}), name='comment-list'),
    url(r'^detail/(?P<pk>\d+)/$', CommentViewSet.as_view({'get': 'retrieve',
                                                          'delete': 'destroy'}), name='comment-detail'),
    url(r'$', CommentViewSet.as_view({'post': 'create'}), name='comment-create'),
]
