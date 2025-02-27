from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(max_length=280)
    add_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post=self).count()

    @property
    def url(self):
        return f"/post/{self.id}/"


class Comment(models.Model):
    content = models.TextField(max_length=280)
    add_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:20]

    class Meta:
        ordering = ['-add_date']
