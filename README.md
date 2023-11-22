

# Финальный проект 4 спринта

## Проверки: Файл **test.py**

1.	`test_add_new_book_add_two_books` - добавление книг в словарь
2.	`test_set_book_genre_set_genre` - установка жанра книги
3.	`test_add_new_book_no_genre` - добавление книги без жанра - у добавленной книги пустой жанр
4.	`test_get_book_genre_get_genre_by_name` - проверка жанра по названию книги
5.	`test_get_books_with_specific_genre_get_comedy_books` - поиск книги по жанру (Комедии)
6.	`test_get_books_genre_all_books` - проверка метода `get_books_genre`
7.	`test_get_books_for_children_all_children_books` - получение списка книг для детей
8.	`test_get_books_for_children_no_adult_books` - Кrниги с возрастным рейтингом отсутствуют в списке книг для детей
9.	`test_add_book_in_favorites_add_two_books` - добавление книг в избранное
10.	`test_get_list_of_favorites_books_all_favorites_books` - проверка метода `get_list_of_favorites_books`
11.	`test_delete_book_from_favorites_one_book_stand` - удаляя одну книгу из избранного, список остается непустым
12.	`test_delete_book_from_favorites_two_no_books_stand` - удаляю две книги из избранного, список пуст

## Фикстуры: Файл **conftest.py**

1. `books_dict` - создание словаря книг для каждого жанра
2. `favorites_books` - создание списка любимых книг