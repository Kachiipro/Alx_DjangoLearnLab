from django.test import TestCase
# tests.py (within the app directory)
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='password')
        
        # Create a book instance to test CRUD operations
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'published_date': '2024-12-01',
           
        }

        self.book = Book.objects.create(**self.book_data)
        self.book_url = reverse('book-detail', args=[self.book.id])
        self.create_url = reverse('book-create')

    def authenticate(self):
        self.client.login(username='testuser', password='password')

        def test_create_book_authenticated(self):
            self.authenticate()
            response = self.client.post(self.create_url, self.book_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(response.data['title'], self.book_data['title'])
            self.assertEqual(response.data['author'], self.book_data['author'])

