"""Helper module to process images TO several dimensions"""
from imagekit import ImageSpec, register
from imagekit.cachefiles import ImageCacheFile
from imagekit.processors import ResizeToFill


class ListThumbnail(ImageSpec):
    processors = [ResizeToFill(45, 67)]
    format = 'JPEG'
    options = {'quality': 85}


def cached_list_thumb(instance):
    # 'image' is the name of the image field on the model
    cached = ''
    if instance.image:
        cached = ImageCacheFile(ListThumbnail(instance.image))
    # only generates the first time, subsequent calls use cache
        cached.generate()
    return cached


class Thumbnail(ImageSpec):
    processors = [ResizeToFill(60, 100)]
    format = 'JPEG'
    options = {'quality': 85}


class MiddlePoster(ImageSpec):
    processors = [ResizeToFill(112, 180)]
    format = 'JPEG'
    options = {'quality': 85}


class Poster(ImageSpec):
    processors = [ResizeToFill(250, 400)]
    format = 'JPEG'
    options = {'quality': 85}


class Featured(ImageSpec):
    processors = [ResizeToFill(830, 475)]
    format = 'JPEG'
    options = {'quality': 85}


register.generator('ic_list_thumbnail', ListThumbnail)
register.generator('ic_thumbnail', Thumbnail)
register.generator('ic_poster', Poster)
register.generator('ic_middle_poster', MiddlePoster)
register.generator('ic_featured', Featured)
