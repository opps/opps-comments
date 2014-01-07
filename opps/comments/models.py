# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey
from mptt.managers import TreeManager

from opps.core.models import NotUserPublishable, OwnedNotRequired


class Comment(MPTTModel, OwnedNotRequired, NotUserPublishable):
    author_name = models.CharField(_(u'Author name'), max_length=255)
    author_email = models.EmailField(_(u'Author email'))
    path = models.CharField(_(u'Path'), max_length=255)
    body = models.TextField(_('Body'))
    parent = TreeForeignKey('self', related_name='replay',
                            null=True, blank=True,
                            verbose_name=_(u'Parent'))

    objects = TreeManager()

    def __unicode__(self):
        return u"{s.author_name} - {s.author_email} - {s.path}".format(
            s=self
        )

    class Meta:
        verbose_name = _(u'Comment')
        verbose_name_plural = _(u'Comments')
