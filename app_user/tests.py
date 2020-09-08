from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.


class AppUserTest(TestCase):
    def test_user(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(username='uname', email='email@email.com',
                                              password='pass', first_name='John',
                                              last_name='Doe')
        self.assertEqual(user.username, 'uname')
        self.assertEqual(user.email, 'email@email.com')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

        self.assertTrue(user.is_active)