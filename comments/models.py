from django.db import models
from django.conf import settings
from posts.models import BlogPost
from livefield import LiveField, LiveManager


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    live = LiveField()

    objects = LiveManager()
    all_objects = LiveManager(include_soft_deleted=True)

    def delete(self, using=None):
        self.live = True
        self.save(using=using)

    def __str__(self):
        return str(self.user)

    @property
    def owner(self):
        return self.user
