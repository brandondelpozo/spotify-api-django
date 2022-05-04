from django.test import TestCase
from django.contrib.auth.models import User
from .models import Album


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
        username='testuser1', password='abc123')
        testuser1.save()
        
        # Create an Album
        test_album = Album.objects.create(
        author=testuser1, title='Album title', body='Body content...')
        test_album.save()
        
    def test_blog_content(self):
        album = Album.objects.get(id=1)
        author = f'{album.author}'
        title = f'{album.title}'
        body = f'{album.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Album title')
        self.assertEqual(body, 'Body content...')