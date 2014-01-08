# coding: utf-8
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from opps.core.admin import PublishableAdmin, apply_opps_rules

from .models import Comment

@apply_opps_rules('comments')
class CommentAdmin(PublishableAdmin):
    list_display = ('author_name', 'author_email', 'body', 'published')
    list_filter = ('published',)
    search_fields = ('author_email',)

    fieldsets = (
        (_(u'Identification'), {
            'fields': ('author_name', 'author_email', 'body', 'path')}),
        (_(u'Relationships'), {
            'fields': ('site', 'mirror_site', 'parent')}),
        (_(u'Publication'), {
            'classes': ('extrapretty'),
            'fields': ('published', 'date_available')}),
    )

    class Meta:
        model = Comment

admin.site.register(Comment, CommentAdmin)
