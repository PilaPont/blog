from django.urls import path
from .views import post_list, post_detail, post_create

urlpatterns = [
    path('', post_list),
    path('create', post_create),
    path('<int:post_id>/', post_detail, name='detail'),
]
