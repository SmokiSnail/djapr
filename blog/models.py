### Django в примерах це в дійсності аналогічно, як в c:\Djex\blog\models.py
### Наш файл в c:\Djapr\blog\models.py практично аналогічний
### blog's model.py

from django.conf import settings             # перша відмінність від djex
from django.db import models
from django.utils import timezone           
##!!!from django.contrib.auth.models import User # друга відмінність

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)


def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title


"""
###  решта зовсім інакше

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    slug = models.SlugField(max_length=250, unique_for_date='publish')
## було    author = models.ForeignKey(User, related_name='blog_posts')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


class Meta:
    ordering = ('-publish',)
"""

