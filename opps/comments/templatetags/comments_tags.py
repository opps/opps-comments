# coding: utf-8

from django.conf import settings
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def load_comments(context):
    """
    OPPS_COMMENTS = {
       "disqus": {
          "shortname": "opps",
       },
       "facebook": {
          "APP_ID": "123456"
       }
    }
    """

    OPPS_COMMENTS = settings.OPPS_COMMENTS
    if not OPPS_COMMENTS:
        return ""

    rendered = []
    for engine, config in OPPS_COMMENTS.iteritems():
        config['request'] = context.get('request')
        template_path = "comments/{0}_comments.html".format(engine)
        t = template.loader.get_template(template_path)
        render = t.render(template.Context(config))
        rendered.append(render)

    return "".join(rendered)


@register.simple_tag
def load_comments_js():
    OPPS_COMMENTS = settings.OPPS_COMMENTS
    if not OPPS_COMMENTS:
        return ""

    rendered = []
    for engine, config in OPPS_COMMENTS.iteritems():
        try:
            template_path = "comments/{0}_comments_js.html".format(engine)
            t = template.loader.get_template(template_path)
            render = t.render(template.Context(config))
            rendered.append(render)
        except template.TemplateDoesNotExist:
            continue

    return "".join(rendered)
