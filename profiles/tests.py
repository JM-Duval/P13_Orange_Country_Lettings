import pytest
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse
from .models import Profile
from django.contrib.auth.models import User
from faker import Faker


@pytest.mark.django_db
class TestProfile:

    def profile(self):
        self.fake = Faker()
        self.user = User.objects.create(username='Testuser')
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city=self.fake.city(),
        )

    def test_profiles_index(self, client):
        self.profile()
        response = client.get('/profiles/')
        assert response.context['profiles_list'][0] == self.profile
        assertTemplateUsed(response, 'profiles_index.html')

    def test_profile(self, client):
        self.profile()
        response = client.get('/profiles/')
        response = client.get(reverse('profiles:profile', kwargs={"username": 'Testuser'}))
        assert response.context['profile'] == self.profile
        assertTemplateUsed(response, 'profile.html')
