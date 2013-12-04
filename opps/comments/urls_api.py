#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from django.conf.urls import patterns, url

from piston.resource import Resource

from .api import CommentHandler


comments = Resource(handler=CommentHandler)

urlpatterns = patterns(
    '',
    url(r'^api/comments/$', comments),
)
