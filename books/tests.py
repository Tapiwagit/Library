from django.test import TestCase
from django.urls import reverse
from .models import Book


# Create your tests here.
class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="TripLe Distilled",
            subtitle="For the Old Bushmills",
            author="Oldman Bushmills",
            isbn="3326451951323",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "TripLe Distilled")
        self.assertEqual(self.book.subtitle, "For the Old Bushmills")
        self.assertEqual(self.book.author, "Oldman Bushmills")
        self.assertEqual(self.book.isbn, "3326451951323")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "For the Old Bushmills")
        self.assertTemplateUsed(response, "books/book_list.html")
