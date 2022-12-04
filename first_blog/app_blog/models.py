from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django_quill.fields import QuillField


class FilmReview(models.Model):
    slug = models.SlugField(unique=True, max_length=50, db_index=True, verbose_name='')
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='')
    content = QuillField(blank=True, verbose_name='')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='')
    time_update = models.DateTimeField(auto_now_add=True, verbose_name='')
    is_published = models.BooleanField(default=True, verbose_name='Publish')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(FilmReview, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Film review'
        verbose_name_plural = 'Film review'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='CATEGORY')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='KEY')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
        ordering = ['id']
