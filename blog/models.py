from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Post Model"""
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """Sets the post to the time of publishing"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
