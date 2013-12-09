# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey
from mptt.managers import TreeManager

from opps.core.models import NotUserPublishable, OwnedNotRequired


class Comment(MPTTModel, OwnedNotRequired, NotUserPublishable):
    author_name = models.CharField(max_length=255)
    author_email = models.EmailField()
    path = models.CharField(max_length=255)
    body = models.TextField()
    parent = TreeForeignKey('self', related_name='replay',
                            null=True, blank=True,
                            verbose_name=_(u'Parent'))

    objects = TreeManager()

    def __unicode__(self):
        return u"{s.author_name} - {s.author_email} - {s.path}".format(
            s=self
        )
