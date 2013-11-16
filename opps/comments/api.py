#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils import timezone

from tastypie.resources import ModelResource

from opps.api import MetaBase

from .models import Comment as CommentModel


class Comment(ModelResource):
    class Meta(MetaBase):
        queryset = CommentModel.objects.filter(
            published=True,
            date_available__lte=timezone.now()
        )