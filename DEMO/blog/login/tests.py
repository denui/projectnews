from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.

class UserTestCase(TestCase):
    """docstring for UserTestCase"""
    def setUp(self):
        User.objects.create(username="haha", password="haha",email ="haha@gmail.com")
        User.objects.create(username="hihi", password="hihi",email ="hihi@gmail.com")




