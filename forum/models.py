from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


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
