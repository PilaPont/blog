
from rest_framework.routers import DefaultRouter

from .views import BlogPostViewSet

router = DefaultRouter()
router.register('', BlogPostViewSet, base_name='posts')
urlpatterns = router.urls
