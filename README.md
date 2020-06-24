# IMDB Clone
## A movie and celebrity info website.
## Live version is at: https://django-imdb-clone.herokuapp.com/

there are screenshots.

## Used technology:
Django, Jquery, Bootstrap

# Please follow the process below to install

1. Clone this repository (use `git clone ...`)

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

# TODOs:
1. Reduce number of queries
2. Registration and login
3. Search functionality
4. Watchlist, favorites and rankings
5. Comments

* rest_framework is introduced to the application, needed base code is written *

*** More unit tests ***

# Other Notes:
1. You may want to remove Google Analytics code.
    Remove this line from templates/html/lte/base.html:
      {% include 'html/lte/_partials/_91_ga.html' %}
    And delete the included html file:
      _91_ga.html