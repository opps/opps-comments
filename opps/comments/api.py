#!/usr/bin/env python
# -*- coding: utf-8 -*-
from opps.api import BaseHandler

from .models import Comment


class CommentHandler(BaseHandler):
    model = Comment
