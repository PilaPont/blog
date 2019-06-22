from rest_framework import serializers

from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    post_title = serializers.ReadOnlyField(source='post.title')
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = [
            'user_name',
            'id',
            'post_title',
            'post',
            'content',
            'created_at',
        ]

    def validate_post(self, post):
        if post.comments.count() >= 3:
            raise serializers.ValidationError("This post is too tired of commenting, then you can't add more comments.")
        return post
