from rest_framework.test import APITestCase, APIRequestFactory
from .views import BlogPostViewSet
from rest_framework import status


class TestPost(APITestCase):
    def SetUp(self):
        self.factory = APIRequestFactory
        self.view = BlogPostViewSet.as_view({'get': 'list'})
        self.uri = '/posts/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.client.credentials(HTTP_AUTHORIZATION=
                                'JWT ' + self.user.get_jwt_token())
        self.assertAlmostEqual(response.status_code, status.HTTP_201_CREATED)
