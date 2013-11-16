#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from django.conf.urls import patterns, url, include
from tastypie.api import Api

from .api import Comment


_api = Api(api_name=u"{}".format("v1"))
_api.register(Comment())


urlpatterns = patterns(
    '',
    url(r'^api/', include(_api.urls)),
)
