import pytest
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse
from .models import Letting, Address
from faker import Faker


@pytest.mark.django_db
class TestLetting:

    def letting(self):
        self.fake = Faker()
        self.address = Address.objects.create(
            number=self.fake.building_number(),
            street=self.fake.street_name(),
            city=self.fake.city(),
            state=self.fake.name(),
            zip_code=self.fake.postcode(),
        )
        self.letting = Letting.objects.create(
            title=self.fake.name(),
            address=self.address
        )

    def test_index(self, client):
        self.letting()
        response = client.get('/lettings/')
        assert response.context['lettings_list'][0] == self.letting
        assertTemplateUsed(response, 'lettings_index.html')

    def test_letting(self, client):
        self.letting()
        response = client.get(reverse('lettings:letting', kwargs={"letting_id": 1}))
        assert response.context['title'] == self.letting.title
        assertTemplateUsed(response, 'letting.html')
