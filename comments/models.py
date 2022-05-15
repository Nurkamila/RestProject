from django.db import models

from account.models import MyUser
from post.models import Post


class Comment(models.Model):
    user = models.ForeignKey(MyUser, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
