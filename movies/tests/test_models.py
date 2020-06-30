"""More tests are written continuously!"""

from django.test import TestCase

from movies.models import Genre, Movie, PgRating


class GenreModelTests(TestCase):
    def setUp(self):
        Genre.objects.create(
            name='Custom Genre', code='CGE',
            content='This is a custom genre for testing.',
            extra_chars_count=3)
        Genre.objects.create(
            name='Another Genre', code='AGE',
            content='Another genre for testing purpose.',
            extra_chars_count=9)

    def test_name_content(self):
        genre = Genre.objects.get(id=1)
        expected_result = genre.name
        self.assertEquals(expected_result, 'Custom Genre')

    def test_code_content(self):
        genre = Genre.objects.get(id=1)
        expected_result = genre.code
        self.assertEquals(expected_result, 'CGE')

    def test_content_content(self):
        genre = Genre.objects.get(id=1)
        expected_result = genre.content
        self.assertEquals(
            expected_result, 'This is a custom genre for testing.')

    def test_extra_chars_count_content(self):
        genre = Genre.objects.get(id=1)
        expected_result = genre.extra_chars_count
        self.assertEquals(expected_result, 3)

    # def test_slug_content(self):
    #     pass


class MovieModelTests(TestCase):
    def setUp(self):
        Movie.objects.create(
            name='Test Movie', original_name='Moviente Teste',
            is_featured=True, release_year=2011, duration=128,
            imdb_rating=5.6, content='Test Movie test content.',
            content_source='https://github.com/pydatageek/imdb-clone',
            trailer='https://www.youtube.com/watch?v=1NJO0jxBtMo',
            trailer_info='full movie',
            # image='',
            image_credit='imdb',
            # pg_rating='', genres='', crews=''
        )
        Movie.objects.create(
            name='Custom Movie 2', original_name='', is_featured=True,
            release_year=2005, duration=111, imdb_rating=7.6,
            content='Custom Movie 2 test content.',
            content_source='https://github.com/pydatageek/imdb-clone',
            trailer='https://www.youtube.com/watch?v=JvwVZaJWrsY',
            trailer_info='great movie',
            # image='',
            image_credit='wikimedia',
            # pg_rating='', genres='', crews=''
        )

    def test_name_content(self):
        movie = Movie.objects.get(id=1)
        expected_result = movie.name
        self.assertEquals(expected_result, 'Test Movie')

    def test_original_name_content(self):
        movie = Movie.objects.get(id=1)
        expected_result = movie.original_name
        self.assertEquals(expected_result, 'Moviente Teste')

    def test_is_featured_content(self):
        movie = Movie.objects.get(id=1)
        expected_result = movie.is_featured
        self.assertEquals(expected_result, True)

    def test_release_year_content(self):
        movie = Movie.objects.get(id=1)
        expected_result = movie.release_year
        self.assertEquals(expected_result, 2011)

    def test_duration_content(self):
        movie = Movie.objects.get(id=1)
        expected_result = movie.duration
        self.assertEquals(expected_result, 128)

    def test_imdb_rating_content(self):
        movie = Movie.objects.get(id=1)
        expected_result = movie.imdb_rating
        self.assertEquals(expected_result, 5.6)

    def test_content_content(self):
        movie = Movie.objects.get(id=1)
        expected_result = movie.content
        self.assertEquals(expected_result, 'Test Movie test content.')

    def test_content_source_content(self):
        movie = Movie.objects.get(id=1)
        expected_result = movie.content_source
        self.assertEquals(
            expected_result, 'https://github.com/pydatageek/imdb-clone')

    def test_trailer_content(self):
        movie = Movie.objects.get(id=1)
        expected_result = movie.trailer
        self.assertEquals(
            expected_result,
            'https://www.youtube.com/watch?v=1NJO0jxBtMo')

    def test_trailer_info_content(self):
        movie = Movie.objects.get(id=1)
        expected_result = movie.trailer_info
        self.assertEquals(expected_result, 'full movie')

    def test_image_credit_content(self):
        movie = Movie.objects.get(id=1)
        expected_result = movie.image_credit
        self.assertEquals(expected_result, 'imdb')

    # def test_slug_content(self):
    #     pass


class PgRatingModelTests(TestCase):
    def setUp(self):
        PgRating.objects.create(
            name='PG Rating for Test', code='PGfT',
            content='PG Rating test content',
            extra_chars_count=7)
        PgRating.objects.create(
            name='Custom second PG Rating', code='CSPGR',
            content='Test content second PG Rating',
            extra_chars_count=5)

    def test_name_content(self):
        pg_rating = PgRating.objects.get(id=1)
        expected_result = pg_rating.name
        self.assertEquals(expected_result, 'PG Rating for Test')

    def test_code_content(self):
        pg_rating = PgRating.objects.get(id=1)
        expected_result = pg_rating.code
        self.assertEquals(expected_result, 'PGfT')

    def test_content_content(self):
        pg_rating = PgRating.objects.get(id=1)
        expected_result = pg_rating.content
        self.assertEquals(expected_result, 'PG Rating test content')

    def test_extra_chars_count_content(self):
        pg_rating = PgRating.objects.get(id=1)
        expected_result = pg_rating.extra_chars_count
        self.assertEquals(expected_result, 7)

    # def test_slug_content(self):
    #     pass
