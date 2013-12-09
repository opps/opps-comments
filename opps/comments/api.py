#!/usr/bin/env python
# -*- coding: utf-8 -*-
from opps.api import BaseHandler

from .models import Comment


class CommentHandler(BaseHandler):
    model = Comment

    def read(self, request):
        def _node(node):
            n = []
            for i in node.get_children():
                if i.published:
                    obj = i.__dict__
                    obj['comments'] = _node(i)
                    n.append(obj)
            return n

        root = self.model.objects.filter(
            level=0,
            published=True).filter(**request.GET.dict())

        l = []
        for t in root:
            n = {}
            n = t.__dict__
            n['comments'] = _node(t)
            l.append(n)

        return l
