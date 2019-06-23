from rest_framework import serializers

from posts.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):  # forms.ModelForm
    username = serializers.ReadOnlyField(source='user.username')
    comments_count = serializers.IntegerField(source='get_comments_count', read_only=True)

    class Meta:
        model = BlogPost
        fields = [
            'id',
            'username',
            'title',
            'content',
            'created_at',
            'updated_at',
            'comments_count'
        ]
        read_only_fields = ['id', 'user']

    def validate_title(self, value):
        qs = BlogPost.objects.filter(title__iexact=value)  # including instance
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This title has already been used")
        return value


