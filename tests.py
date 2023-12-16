import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize(
        'incorrect_len_book_name, status',
        [
            ['', None],
            ['Самое длинное название книги в мире за все время', None]
        ]
    )
    def test_add_new_book_with_incorrect_parameters(self, incorrect_len_book_name, status):
        collector = BooksCollector()
        collector.add_new_book(incorrect_len_book_name)
        book_from_collector = collector.books_genre.get(incorrect_len_book_name)
        assert book_from_collector == status

    def test_add_existing_book_in_dictionary(self):
        collector = BooksCollector()

        test_book_name = 'Mowgli'
        test_genre = collector.genre[3]

        collector.add_new_book(test_book_name)
        collector.set_book_genre(test_book_name, test_genre)

        collector.add_new_book(test_book_name)

        assert collector.get_book_genre(test_book_name)

    def test_add_genre_to_book(self):
        collector = BooksCollector()

        test_book_name = 'Dune'
        test_genre = collector.genre[0]

        collector.add_new_book(test_book_name)
        collector.set_book_genre(test_book_name, test_genre)

        actual = collector.books_genre.get(test_book_name)
        assert test_genre == actual

    def test_add_not_existing_genre_to_book(self):
        collector = BooksCollector()

        test_book_name = 'The Catcher in the Rye'
        not_existing_genre = 'Роман'

        collector.add_new_book(test_book_name)
        collector.set_book_genre(test_book_name, not_existing_genre)

        actual = collector.books_genre.get(test_book_name)
        assert actual == ''

    def test_get_genre_by_book_name(self):
        collector = BooksCollector()

        test_book_name = 'Shining'
        test_genre = collector.genre[1]

        collector.add_new_book(test_book_name)
        collector.set_book_genre(test_book_name, test_genre)

        actual = collector.get_book_genre(test_book_name)
        assert test_genre == actual

    def test_get_specific_genre_for_three_books(self):
        collector = BooksCollector()

        horror_genre = collector.genre[1]
        horror_book_list = [
            'Pet Sematary',
            'Call of Cthulhu',
            'Dracula',
        ]

        for book in horror_book_list:
            collector.add_new_book(book)
            collector.set_book_genre(book, horror_genre)

        actual = collector.get_books_with_specific_genre(horror_genre)
        assert horror_book_list == actual

    def test_get_all_genres_from_dictionary(self):
        collector = BooksCollector()

        strugatsky_books = {
            'Roadside Picnic': 'Фантастика',
            'Hard to be a god': 'Фантастика'
        }
        for (book, genre) in strugatsky_books.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        actual = collector.get_books_genre()
        assert strugatsky_books == actual

    def test_book_list_for_children(self):
        collector = BooksCollector()

        different_books = {
            'Little Prince': 'Мультфильмы',
            'Silence of the Lambs': 'Детектив'
        }

        for (book, genre) in different_books.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        actual = collector.get_books_for_children()

        for book in actual:
            genre = different_books.get(book)
            assert genre not in collector.genre_age_rating

    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        favorite_book = 'Holy Book'
        collector.add_new_book(favorite_book)
        collector.add_book_in_favorites(favorite_book)

        assert favorite_book in collector.favorites

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        least_favorite_book = 'Cooking Book'
        collector.add_new_book(least_favorite_book)
        collector.add_book_in_favorites(least_favorite_book)
        collector.delete_book_from_favorites(least_favorite_book)

        assert least_favorite_book not in collector.favorites

    def test_get_favorite_book_list(self):
        collector = BooksCollector()

        favorite_book = [
            'Lolita',
            'A Young Doctor_s Notebook'
        ]
        for book in favorite_book:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        actual = collector.get_list_of_favorites_books()
        assert favorite_book == actual
