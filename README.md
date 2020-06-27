# Django IMDB Clone
## A movie and celebrity info website.
## Live version is at: https://django-imdb-clone.herokuapp.com/

there are screenshots: https://github.com/pydatageek/imdb-clone/tree/master/screenshots/

## Used technology:
Django (Python) + Jquery, Bootstrap

# Please follow the process below to install

1. Clone this repository (use `git clone https://github.com/pydatageek/imdb-clone.git`)

### setting up a development environment
2. start an environment with requirements
   e.g. pipenv install -r <project-folder>/requirements.txt

### migrating the already defined models and creating the super user
3. python manage.py migrate

### super user should be created before the dummy data be loaded!
4. python manage.py createsuperuser

### loading dummy data
5. python manage.py loaddata data.json

### collectstatic -> required/needed for ckeditor (wysiwyg editor) 
6. python manage.py collectstatic

P.S: you may follow the process as the ordering defined or there may be problems with user related data


# Version History:
## 0.1.1
Simple search functionality

## 0.1.0
First commit


# TODOs:
1. Reduce number of queries
2. Registration and login
3. Watchlist, favorites and rankings
4. Comments
5. Performance improvements on search

* rest_framework is introduced to the application, needed base code is written, but not secure yet *

* More unit tests are added continuously *

# Other Notes:
1. You may want to remove Google Analytics code.
    Remove this line from templates/html/lte/base.html:
      {% include 'html/lte/_partials/_91_ga.html' %}
    And delete the included html file:
      _91_ga.html