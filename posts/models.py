from django.conf import settings
from django.db import models


class BlogPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=True, blank=True)
    content = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    @property
    def owner(self):
        return self.user

    # comments_count = computed_property.ComputedIntegerField(compute_from='get_comments_count')

    @property
    def get_comments_count(self):
        return self.comments.count()
