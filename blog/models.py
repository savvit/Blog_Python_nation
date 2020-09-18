from django.db import models
from django.urls import reverse
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
"""
Category
=====
title, slug
"""


"""
Tag
=====
title, slug
"""


"""
Post
=====
title, slug, content, date, img, views, category, tags
"""


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, verbose_name='URL категории', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=15)
    slug = models.SlugField(max_length=15, verbose_name='Tag URL', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255)
    tetssfield = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL поста')
    content = RichTextUploadingField()
    time_to_read = models.PositiveIntegerField(default=0, verbose_name='Время для прочтения')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    img = models.ImageField(upload_to='media', default='default.jpg')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('getpost', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created']
