import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize('book_list', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])
    def test_add_new_book_add_two_books(self, book_list):
        collector = BooksCollector()
        collector.add_new_book(book_list)
        assert book_list in collector.get_books_genre()

    def test_set_book_genre_set_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Корабль призрак')
        collector.set_book_genre('Корабль призрак', 'Фантастика')
        assert collector.get_book_genre('Корабль призрак') == 'Фантастика'

    def test_add_new_book_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оппенгеймер')
        assert collector.get_book_genre('Оппенгеймер') == ''

    def test_get_book_genre_get_genre_by_name(self, books_dict):
        assert books_dict.get_book_genre('Прекрасные дни') == 'Детективы'

    def test_get_books_with_specific_genre_get_comedy_books(self, books_dict):
        assert books_dict.get_books_with_specific_genre('Комедии') == ['Бесконечный бассейн']

    def test_get_books_genre_all_books(self, books_dict):
        assert books_dict.get_books_genre() == {'Корабль призрак': 'Фантастика', 'Оппенгеймер': 'Ужасы', 'Прекрасные дни': 'Детективы', 'Одержимые злом': 'Мультфильмы', 'Бесконечный бассейн': 'Комедии'}

    def test_get_books_for_children_all_children_books(self, books_dict):
        assert books_dict.get_books_for_children() == ['Корабль призрак', 'Одержимые злом', 'Бесконечный бассейн']

    @pytest.mark.parametrize('adult_books', ['Оппенгеймер', 'Прекрасные дни'])
    def test_get_books_for_children_no_adult_books(self, books_dict, adult_books):
        assert adult_books not in books_dict.get_books_for_children()

    @pytest.mark.parametrize('favor_books', ['Корабль призрак', 'Оппенгеймер'])
    def test_add_book_in_favorites_add_two_books(self, favor_books, books_dict):
        books_dict.add_book_in_favorites(favor_books)
        assert favor_books in books_dict.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_all_favorites_books(self, books_dict, favorites_books):
        assert books_dict.get_list_of_favorites_books() == ['Корабль призрак', 'Оппенгеймер']

    def test_delete_book_from_favorites_one_book_stand(self, books_dict, favorites_books):
        books_dict.delete_book_from_favorites('Корабль призрак')
        assert books_dict.get_list_of_favorites_books() == ['Оппенгеймер']

    def test_delete_book_from_favorites_two_no_books_stand(self, books_dict, favorites_books):
        books_dict.delete_book_from_favorites('Корабль призрак')
        books_dict.delete_book_from_favorites('Оппенгеймер')
        assert books_dict.get_list_of_favorites_books() == []

