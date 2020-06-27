"""More tests are written continuously!"""
from datetime import date
import random
import string

from unidecode import unidecode

from django.test import TestCase
from django.utils import timezone

from celebs.models import Celebrity, Duty


def random_chars(counts):
    return ''.join(['{}'.format(
        random.choice(string.ascii_lowercase + string.digits))
        for _ in range(counts)])

# self.slug = slugify(unidecode(self.name))


class CelebrityModelTests(TestCase):
    def setUp(self):
        Celebrity.objects.create(
            name='Adam Smith', first_name='Adam', last_name='Smith',
            nick_name='AS', is_featured=False, birthdate=date(1723, 6, 16),
            birth_place='Kirkcaldy, Fife, Scotland',
            deathdate=date(1790, 7, 17), death_place='Edinburgh, Scotland',
            content='Adam Smith, a Scottish economist, philosopher, and author is known as The Father of Economics.',
            content_source='https://en.wikipedia.org/wiki/Adam_Smith',
            trailer='https://www.youtube.com/watch?v=1NJO0jxBtMo',
            trailer_info='',
            # image='',
            image_credit='wikimedia.org',
            # duties=''
        )
        Celebrity.objects.create(
            name='Selma Soysal', first_name='Selma', last_name='Soysal',
            nick_name='SS', is_featured=True, birthdate=date(1924, 1, 1),
            birth_place='Zonguldak, Turkey', deathdate=date(2011, 10, 10),
            death_place='İstanbul, Turkey',
            content='One of the first Turkish female mathematicians.',
            content_source='https://tr.wikipedia.org/wiki/Selma_Soysal',
            trailer='https://www.youtube.com/watch?v=JvwVZaJWrsY',
            trailer_info='No info',
            # image='',
            image_credit='wikimedia.org',
            # duties=''
        )

        # random_chars = random_chars(self.extra_chars_count)

    def test_name_content(self):
        celeb = Celebrity.objects.get(id=1)
        expected_result = celeb.name
        self.assertEquals(expected_result, 'Adam Smith')

    def test_first_name_content(self):
        celeb = Celebrity.objects.get(id=1)
        expected_result = celeb.first_name
        self.assertEquals(expected_result, 'Adam')

    def test_last_name_content(self):
        celeb = Celebrity.objects.get(id=1)
        expected_result = celeb.last_name
        self.assertEquals(expected_result, 'Smith')

    def test_nick_name_content(self):
        celeb = Celebrity.objects.get(id=1)
        expected_result = celeb.nick_name
        self.assertEquals(expected_result, 'AS')

    def test_is_featured_content(self):
        celeb = Celebrity.objects.get(id=1)
        expected_result = celeb.is_featured
        self.assertEquals(expected_result, False)

    def test_birthdate_content(self):
        celeb = Celebrity.objects.get(id=1)
        expected_result = celeb.birthdate
        self.assertEquals(expected_result, date(1723, 6, 16))

    def test_birth_place_content(self):
        celeb = Celebrity.objects.get(id=1)
        expected_result = celeb.birth_place
        self.assertEquals(expected_result, 'Kirkcaldy, Fife, Scotland')

    def test_deathdate_content(self):
        celeb = Celebrity.objects.get(id=1)
        expected_result = celeb.deathdate
        self.assertEquals(expected_result, date(1790, 7, 17))

    def test_death_place_content(self):
        celeb = Celebrity.objects.get(id=1)
        expected_result = celeb.death_place
        self.assertEquals(expected_result, 'Edinburgh, Scotland')

    def test_content_content(self):
        celeb = Celebrity.objects.get(id=1)
        expected_result = celeb.content
        self.assertEquals(
            expected_result,
            'Adam Smith, a Scottish economist, philosopher, and author is known as The Father of Economics.')

    def test_content_source_content(self):
        celeb = Celebrity.objects.get(id=1)
        expected_result = celeb.content_source
        self.assertEquals(
            expected_result,
            'https://en.wikipedia.org/wiki/Adam_Smith')

    def test_trailer_content(self):
        celeb = Celebrity.objects.get(id=1)
        expected_result = celeb.trailer
        self.assertEquals(
            expected_result,
            'https://www.youtube.com/watch?v=1NJO0jxBtMo')

    def test_trailer_info_content(self):
        celeb = Celebrity.objects.get(id=1)
        expected_result = celeb.trailer_info
        self.assertEquals(expected_result, '')

    def test_image_credit_content(self):
        celeb = Celebrity.objects.get(id=1)
        expected_result = celeb.image_credit
        self.assertEquals(expected_result, 'wikimedia.org')

    # def test_slug_content(self):
    #     celeb = Celebrity.objects.get(id=1)
    #     expected_result = celeb.slug
    #     self.assertEquals(
    #         expected_result,
    #         f'{celeb.first_name.lower()}-{celeb.last_name.lower()}-{random_chars(5)}')


class DutyModelTests(TestCase):
    def setUp(self):
        Duty.objects.create(
            name='Custom Duty', code='C',
            extra_chars_count=5)
        Duty.objects.create(
            name='Test Duty 2', code='T',
            extra_chars_count=3)

    def test_name_content(self):
        duty = Duty.objects.get(id=1)
        expected_result = duty.name
        self.assertEquals(expected_result, 'Custom Duty')

    def test_code_content(self):
        duty = Duty.objects.get(id=1)
        expected_result = duty.code
        self.assertEquals(expected_result, 'C')

    def test_extra_chars_count_content(self):
        duty = Duty.objects.get(id=1)
        expected_result = duty.extra_chars_count
        self.assertEquals(expected_result, 5)

    # def test_slug_content(self):
    #     pass
