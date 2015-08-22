=====
django-scout
=====

django-scout is a django package to conduct Web-based survey. 

Set of surveys can be created with specified set of questions and answer types.

Quick start
-----------

1. Add "django-scout" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'survey',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^survey/', include('survey.urls')),

3. Run `python manage.py migrate` to create the survey models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a survey with set of questions of certain types.

