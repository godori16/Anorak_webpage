# from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
    )
    thumbnail_image = models.ImageField(upload_to='blog_thumbnails/', blank=True, default='default.jpg')
    thumbnail_text = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])

class Comment(models.Model):
    article = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE,
        related_name='comments')
    comment = models.CharField(max_length=200)
    author = models.ForeignKey(
        # settings.AUTH_USER_MODEL,
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('blog_list')