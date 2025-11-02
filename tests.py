import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
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

    def test_get_book_genre_returns_dictionary(self):
        collector = BooksCollector()
        genre_dict = collector.get_books_genre()

        assert isinstance(genre_dict, dict)

    def test_get_books_genre_empty_dictionary(self):
        collector = BooksCollector()
        genre_dict = collector.get_books_genre()

        assert genre_dict == {}

#добавил две проверки для get_books_genre

    def test_set_new_genre_fantastic(self):
        collector = BooksCollector()
        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Ведьмак', 'Фантастика')
        
        assert collector.get_book_genre('Ведьмак') == 'Фантастика'

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Лолита')
        collector.set_book_genre('Лолита', 'Несуществующий жанр')

        assert collector.get_book_genre('Лолита') == ''

    def test_set_book_genre_incorrect_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Неизвестный жанр')
        
        assert collector.get_book_genre('Гордость и предубеждение') == ''


    def test_get_books_with_specific_genre_comedy(self):
        collector = BooksCollector()
        collector.add_new_book('Юмористические рассказы')
        collector.set_book_genre('Юмористические рассказы', 'Комедии')
        
        assert collector.get_books_with_specific_genre('Комедии') == ['Юмористические рассказы']

    def test_get_books_for_children_neznaika(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка на луне')
        collector.set_book_genre('Незнайка на луне', 'Комедии')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        
        assert collector.get_books_for_children() == ['Незнайка на луне']

    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_book_in_favorites('Гордость и предубеждение')

        assert 'Гордость и предубеждение' in collector.favorites

    def test_add_book_in_favorites_not_in_books(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Книга которой нет')

        assert 'Книга которой нет' not in collector.favorites

    def test_add_book_in_favorites_multiple_times(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        
        assert collector.get_list_of_favorites_books().count('Мастер и Маргарита') == 1

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Братья Карамазовы')
        collector.add_book_in_favorites('Братья Карамазовы')
        collector.delete_book_from_favorites('Братья Карамазовы')
        
        assert 'Братья Карамазовы' not in collector.favorites

    @pytest.mark.parametrize('name', ['Одиссея', 'Идиот', 'Герой нашего времени'])

    def test_get_list_of_favorites_books_success(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
      
        assert collector.get_list_of_favorites_books() == [name]


