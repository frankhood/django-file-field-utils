=====
Usage
=====

To use Django File Field Utils in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'file_field_utils.apps.FileFieldUtilsConfig',
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
