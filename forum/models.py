from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=60)
    user = models.ForeignKey(User, models.CASCADE)

    def get_absolute_url(self):
        return reverse('post', kwargs={'year': self.pub_date.year,
                                       'month': self.pub_date.month,
                                       'slug': self.slug})

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()
