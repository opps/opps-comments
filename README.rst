OPPS-COMMENTS
=============

Install
-------

.. code-block:: bash

    pip install -e git+https://github.com/opps/opps-comments.git#egg=opps-comments



Configuration
-------------

Include `opps.comments` on your django settings:

.. code-block:: python

    INSTALLED_APPS += (
        'opps.comments',
    )


Add Opps Comments credentials on your django settings:

.. code-block:: python

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

.. code-block:: html

    {% load comments_tags %}
    {% load_comments %}
