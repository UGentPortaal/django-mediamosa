================
django-mediamosa
================

django integration for a mediamosa (http://www.mediamosa.org) api.

Currently this version only support setting up the API in settings.py
and has some examples in the urls.py and views.py file to illustrate how
this can be used.

------------
Installation
------------

Install django-mediamosa as follows:

::

   pip install django-mediamosa


-------------
Configuration
-------------

Add the following config to your project's settings.py:

.. code:: python

    MEDIAMOSA_URL = 'http://apivideo.example.com'
    MEDIAMOSA_USERNAME = 'USERNAME'
    MEDIAMOSA_PASSWORD = 'PASSWORD'

-----
Usage
-----

You can start using the api in your views by importing the 'api' object
as follows:

.. code:: python

    from django_mediamosa.base import api

-------------------------
Bugs and Feature requests
-------------------------

For help, issues and feature requests, please go to http://www.github.com/UGentPortaal/django-mediamosa.

------------
Contributing
------------

Pull requests may be submitted to the develop branch at our github
project. Make sure the code and functionality are sufficiently
documented.