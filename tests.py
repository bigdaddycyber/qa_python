import pytest 

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Твин Пикс')
        collector.add_new_book('Карлсон')
        assert len(collector.get_books_genre()) == 2
        
    def test_get_book_genre(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Детективы')    
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Детективы'
        
    def test_get_books_with_specific_genre(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Детективы')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Фантастика')
        assert collector.get_books_with_specific_genre('Детективы') == ['Гордость и предубеждение и зомби'] 

    def test_get_books_genre(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Детективы')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Фантастика')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Детективы', 'Что делать, если ваш кот хочет вас убить': 'Фантастика' }
        
    def test_get_books_for_children(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Крошка - коврошка')
        collector.set_book_genre('Крошка - коврошка', 'Мультфильмы')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Фантастика')
        assert collector.get_books_for_children() == ['Крошка - коврошка']

    def test_add_book_in_favorites(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']
        
    def test_delete_book_from_favorites(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []
        
    def test_get_list_of_favorites_books(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']
        