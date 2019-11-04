=====
Rest Todo Api
=====

Rest Todo Api is a simple Django rest app to use todo api.

Quick start
-----------
1. Add 'rest_todo_api', 'rest_framework', 'django_filters' to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'rest_framework',
        'django_filters',
        'rest_todo_api',
    ]

2. Add settings for Rest Framework like this::

    REST_FRAMEWORK = {
        'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

        # Add 'DEFAULT_PAGINATION_CLASS' and 'PAGE_SIZE', if you want paginate tasks.
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 10
    }

3. Include the rest_todo_api URLconf in your project urls.py like this::

    from rest_todo_api.urls import router as rest_todo_api_router

    urlpatterns = [
      ...
      url(r'^api/todo/', include(rest_todo_api_router.urls)),
    ]

4. Run `python manage.py migrate` to create the rest_todo_api models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create some status, tags, then tasks (you'll need the Admin app enabled).

   ex)
   status {
      "value": "TODO",
      "value": "DOING",
      "value": "DONE"
   }

   tags {
      "value": "Bussiness",
      "value": "Shopping"
   }

6. Visit http://127.0.0.1:8000/api/ to see api resources.