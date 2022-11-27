from unittest.mock import MagicMock

import pytest

from dao.model.movie import Movie
from dao.model.genre import Genre
from dao.model.director import Director
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title="title-1", description="description-1", trailer="trailer-1", year=1, rating=1.1, genre_id=1, director_id=1)
    movie_2 = Movie(id=2, title="title-2", description="description-2", trailer="trailer-2", year=2, rating=2.1, genre_id=2, director_id=2)
    movie_3 = Movie(id=3, title="title-3", description="description-3", trailer="trailer-3", year=3, rating=3.1, genre_id=3, director_id=3)

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock(return_value=None)
    movie_dao.update = MagicMock()
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            "id": 3,
            "title": "title-3",
            "description": "description-3",
            "trailer": "trailer-3",
            "year": 3,
            "rating": 3.1,
            "genre_id": 3,
            "director_id": 3
        }

        movie = self.movie_service.create(movie_d)

        assert movie.id is not None

    def test_delete(self):
        movie = self.movie_service.delete(1)

        assert movie is None

    def test_update(self):
        movie_d = {
            "id": 3,
            "title": "title-3",
            "description": "description-3",
            "trailer": "trailer-3",
            "year": 3,
            "rating": 3.1,
            "genre_id": 3,
            "director_id": 3
        }

        movie = self.movie_service.update(movie_d)

        assert movie.id is not None
