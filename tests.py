from main import BooksCollector

import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    @pytest.mark.parametrize("book_name", [
        "Гордость и предубеждение и зомби",
        "Что делать, если ваш кот хочет вас убить"
    ])
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, book_name):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize("book_name", [
        "Оно"
    ])
    def test_add_new_book_twice(self, book_name): # добавление книги дважды

        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.add_new_book(book_name)

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize("book_name, genre", [
        ("Оно", "Ужасы")
    ])
    def test_get_book_genre(self, book_name, genre): # привязка жанра к книге

        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert collector.get_book_genre(book_name) == genre

    def test_set_book_genre(self):  # устанавливаем жанр книге
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_get_books_with_specific_genre(self): # выводим книги с определенным жанром

        collector = BooksCollector()

        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        horror_books = collector.get_books_with_specific_genre('Ужасы')
        assert 'Оно' in horror_books

    def test_get_books_for_children(self):  # получаем книги, подходящие детям
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')


        books_for_children = collector.get_books_for_children()
        assert 'Гордость и предубеждение и зомби' in books_for_children

    def test_add_book_in_favorites(self): # добавляем книгу в избранное

        collector = BooksCollector()

        collector.add_new_book('Грозовой перевал')
        collector.add_book_in_favorites('Грозовой перевал')

        assert 'Грозовой перевал' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_without_genre(self): # добавляем в избранное книгу без жанра
        collector = BooksCollector()
        collector.add_new_book('Старик и море')

        collector.add_book_in_favorites('Старик и море')

        assert 'Старик и море' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_twice(self): # добавление книги дважды в избранное
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')

        collector.add_book_in_favorites('1984')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self): # удаляем книгу из избранного
        collector = BooksCollector()
        collector.add_book_in_favorites('1984')

        collector.delete_book_from_favorites('1984')

        assert '1984' not in collector.get_list_of_favorites_books()


    def test_delete_non_existent_book_from_favorites(self): # удаляем уже ранее удаленную книгу из избранного
        collector = BooksCollector()

        collector.delete_book_from_favorites('1984')

        assert len(collector.favorites) == 0


    def test_get_list_of_favorites_books(self): # получение списка избранных книг
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')

        assert collector.get_list_of_favorites_books() == ['1984']
    def test_add_new_book_with_long_title(self): # в названии больше 40 символов
        collector = BooksCollector()
        collector.add_new_book('Мы' * 41)

        assert len(collector.get_books_genre()) == 0