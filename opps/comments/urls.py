#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from django.conf.urls import patterns, url

from .views import CommentsView


urlpatterns = patterns(
    '',
    url(
        r'^(?P<path>[\w//\-.]+)$',
        CommentsView.as_view(),
        name='comments'
    ),
)
