"""Project-wide re-usable helper functions"""

import os
import random
import string

from datetime import date, datetime

from django.db import models
from django.core.validators import ValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def get_age(birth_date, death_date=None):
    """returns the age of thing/person or else from its birth_date"""
    today = timezone.now()

    if death_date and isinstance(death_date, (date, datetime)):
        today = death_date

    if birth_date:
        if isinstance(birth_date, (date, datetime)):
            age_computed = today.year - birth_date.year - (
                (today.month, today.day) < (
                    birth_date.month, birth_date.day))
            return age_computed
        elif isinstance(birth_date, (int,)):
            age_computed = int(today.year) - birth_date
            return age_computed
    return ''


def get_duration_humanize(duration):
    """Returns the duration of a movie in hours and minutes"""
    hours = duration // 60
    minutes = duration % 60
    return f'{hours}h {minutes}min'


def get_extension(filename):
    """Returns the extension of a file."""
    return os.path.splitext(filename)


def random_chars(counts):
    """Generates 'counts' number random chars consisting of letters 
    and numbers.
    TODO: a higher performance way?
    """
    return ''.join(['{}'.format(
        random.choice(string.ascii_lowercase + string.digits))
        for _ in range(counts)])


def video_code(url):
    """It returns video specific code from url to be used in apps easily
    e.g. for a youtube video it is: 695y8rdHsA4
    TODO: make the code more robust
    """
    if url is None or str(url).strip() == '':
        # TODO: what will happen if there is no video
        return 'no-video'
    else:
        if str(url).find('youtube.com') != -1:  # for youtube
            splitted = url.split('watch?v=')[1]
            code = splitted.split('&')[0] if splitted.find('&') else splitted
            link = 'https://www.youtube.com/embed/' + str(code)
            image = f'https://img.youtube.com/vi/{code}/maxresdefault.jpg'
            return (link, image, 'youtube')
        elif str(url).find('vimeo.com') != -1:  # for vimeo
            splitted = url.split('vimeo.com/')[1]
            code = splitted  # add other controls
            link = 'https://player.vimeo.com/video/' + str(code)
            # image = 'https://vimeo.com/api/oembed.json?url=https://vimeo.com/' + \
            #     str(code)['thumbnail_url']
            image = ''
            return (link, image, 'vimeo')
        elif str(url).find('dailymotion.com') != -1:  # for dailymotion
            splitted = url.split('/')[-1]
            code = splitted.split('?')[0] if splitted.find('?') else splitted
            link = 'https://www.dailymotion.com/embed/video/' + str(code)
            image = 'https://www.dailymotion.com/thumbnail/video/' + code
            return (link, image, 'dailymotion')
        else:
            return 'no-video'
