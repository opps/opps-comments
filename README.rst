OPPS-COMMENTS
=============

Install
-------

.. block-code:: bash

    pip install -e git+https://github.com/opps/opps-comments.git#egg=opps-comments



Configuration
-------------

Include `opps.comments` on your django settings:

.. block-code:: python

    INSTALLED_APPS += (
        'opps.comments',
    )

Add Opps Comments credentials on your django settings:

.. block-code:: python

    OPPS_COMMENTS = {
        "disqus": {
            "shortname": "opps",
        },
        "facebook": {
            "APP_ID": "123456"
        }
    }



Used
----

.. block-code:: html

    {% load comments_tags %}
    {% load_comments %}
