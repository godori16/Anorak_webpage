# Generated by Django 3.0.4 on 2020-03-27 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200327_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail_image',
            field=models.ImageField(blank=True, default='static/imgs/blog/nature1.jpg', upload_to='blog_thumbnails/'),
        ),
    ]