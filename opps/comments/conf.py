# coding: utf-8

from appconf import AppConf


class OppsCommentsConf(AppConf):
    COMMENTS = {}

    class Meta:
        prefix = "opps"
