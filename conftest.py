import pytest
from main import BooksCollector


@pytest.fixture
def books_dict():
    collector = BooksCollector()
    collector.add_new_book('Корабль призрак')
    collector.set_book_genre('Корабль призрак', 'Фантастика')
    collector.add_new_book('Оппенгеймер')
    collector.set_book_genre('Оппенгеймер', 'Ужасы')
    collector.add_new_book('Прекрасные дни')
    collector.set_book_genre('Прекрасные дни', 'Детективы')
    collector.add_new_book('Одержимые злом')
    collector.set_book_genre('Одержимые злом', 'Мультфильмы')
    collector.add_new_book('Бесконечный бассейн')
    collector.set_book_genre('Бесконечный бассейн', 'Комедии')
    return collector


@pytest.fixture
def favorites_books(books_dict):
    books_dict.add_book_in_favorites('Корабль призрак')
    books_dict.add_book_in_favorites('Оппенгеймер')
    return books_dict.favorites