from django.db import models

class Data(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
    )
    thumbnail_image = models.ImageField(upload_to='static/uploads/data', default='static/imgs/blog/nature1.jpg')
    thumbnail_text = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title