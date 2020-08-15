from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    link = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.PositiveIntegerField(default=0)
    author_name = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    author_name = models.CharField(max_length=60)
    content = models.CharField(max_length=120)
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
