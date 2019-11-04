=====
Rest Todo Api
=====

Rest Todo Api is a simple Django rest app to use todo api.

Quick start
-----------
1. Install django-rest-todo-api by pip.
  $ pip install https://github.com/Saknowman/django-rest-todo-api/raw/master/dist/django-rest-todo-api-0.1.tar.gz

2. Add 'rest_todo_api', 'rest_framework', 'django_filters' to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'rest_framework',
        'django_filters',
        'rest_todo_api',
    ]

3. Add settings for Rest Framework like this::

    REST_FRAMEWORK = {
        'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

        # Add 'DEFAULT_PAGINATION_CLASS' and 'PAGE_SIZE', if you want paginate tasks.
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 10
    }

4. Include the rest_todo_api URLconf in your project urls.py like this::

    from rest_todo_api.urls import router as rest_todo_api_router

    urlpatterns = [
      ...
      url(r'^api/todo/', include(rest_todo_api_router.urls)),
    ]

5. Run `python manage.py migrate` to create the rest_todo_api models.

6. Start the development server and visit http://127.0.0.1:8000/admin/
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

7. Visit http://127.0.0.1:8000/api/ to see api resources.
