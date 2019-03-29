from django.db import models
from django.utils import timezone


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Topic(models.Model):
    title = models.CharField(max_length=100)
    topic_text = models.CharField(max_length=350)
    pub_date = models.DateTimeField(default=timezone.now)
    user = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    user = models.CharField(max_length=30, default='user')
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment_text

