import pytest

from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Детективы')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Фантастика')
    collector.add_new_book('Крошка - коврошка')
    collector.set_book_genre('Крошка - коврошка', 'Мультфильмы')
    return collector 
    