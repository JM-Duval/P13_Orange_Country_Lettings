import pytest
from django.test import Client
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
            user = self.user,
            favorite_city = self.fake.city(),
        )

    def test_profiles_index(self, client):
        self.profile()
        response = client.get('/profiles/')
        assert response.context['profiles_list'][0] == self.profile
        assertTemplateUsed(response, 'profiles_index.html')        

    def test_profile(self, client):
        self.profile()
        response = client.get('/profiles/')
        response = client.get(reverse('profiles:profile', kwargs={"username":'Testuser'}))
        assert response.context['profile'] == self.profile
        assertTemplateUsed(response, 'profile.html')

"""
@pytest.mark.django_db
def test_profiles_index(client):
    fake = Faker()
    user = User.objects.create(username='Testuser')
    profile = Profile.objects.create(
        user = user,
        favorite_city = fake.city(),
        )
    response = client.get('/profiles/')
    print(response.context['profiles_list'][0])
    assert response.context['profiles_list'][0] == profile
    assertTemplateUsed(response, 'profiles_index.html')        

@pytest.mark.django_db
def test_profile(client): #profile.html  
    fake = Faker()
    user = User.objects.create(username='Testuser')
    profile = Profile.objects.create(
        user = user,
        favorite_city = fake.city(),
        )
    response = client.get('/profiles/')
    response = client.get(reverse('profiles:profile', kwargs={"username":'Testuser'}))
    print(response.context['profile'])
    print(profile)
    assert response.context['profile'] == profile
    assertTemplateUsed(response, 'profile.html')
"""
