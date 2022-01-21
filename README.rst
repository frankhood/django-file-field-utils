=============================
Django File Field Utils
=============================

.. image:: https://badge.fury.io/py/django-file-field-utils.svg/?style=flat-square
    :target: https://badge.fury.io/py/django-file-field-utils

.. image:: https://readthedocs.org/projects/pip/badge/?version=latest&style=flat-square
    :target: https://django-file-field-utils.readthedocs.io/en/latest/

.. image:: https://img.shields.io/coveralls/github/frankhood/django-file-field-utils/main?style=flat-square
    :target: https://coveralls.io/github/frankhood/django-file-field-utils?branch=main
    :alt: Coverage Status

This package is a set of field and widget that improves the images and files field behaviour

Documentation
-------------

The full documentation is at https://django-file-field-utils.readthedocs.io.

Quickstart
----------

Install Django File Field Utils::

    pip install django-file-field-utils

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'file_field_utils',
        ...
    )

Add Django File Field Utils's URL patterns:

.. code-block:: python

    from file_field_utils import urls as file_field_utils_urls


    urlpatterns = [
        ...
        url(r'^', include(file_field_utils_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
