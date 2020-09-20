from django.test import TestCase
from .models import  Author

# Create your tests here.


class AuthorTest(TestCase):
    def test_author_model(self):
        author = Author.objects.create(name="Harper", surname='Lee')
        self.assertEqual(author.name, 'Harper')
        self.assertEqual(author.surname, 'Lee')

