from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    #Se sobre escribe el método setUp 
    def setUp(self):
        User.objects.create_user('test', 'test@test.com', 'test1234')        

    #El nombre debe empezar con test_ 
    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True)