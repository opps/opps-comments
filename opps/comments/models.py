# coding: utf-8

from django.db import models
from opps.core.models import NotUserPublishable, OwnedNotRequired


class Comment(OwnedNotRequired, NotUserPublishable):
    author_name = models.CharField(max_length=255)
    author_email = models.EmailField()
    path = models.CharField(max_length=255)
    body = models.TextField()

    def __unicode__(self):
        return u"{s.author_name} - {s.author_email} - {s.path}".format(
            s=self
        )
