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
            number = self.fake.building_number(),
            street = self.fake.street_name(),
            city = self.fake.city(),
            state = self.fake.name(),
            zip_code = self.fake.postcode(),
        )
        self.letting = Letting.objects.create(
            title = self.fake.name(), 
            address = self.address
        )

    def test_index(self, client):
        self.letting()
        response = client.get('/lettings/')
        assert response.context['lettings_list'][0] == self.letting
        assertTemplateUsed(response, 'lettings_index.html')    

    def test_letting(self, client):
        self.letting()
        response = client.get(reverse('lettings:letting', kwargs={"letting_id":1}))
        #print(response.content.decode())
        assert response.context['title'] == self.letting.title
        assertTemplateUsed(response, 'letting.html')


















"""
@pytest.mark.django_db
class Test_Letting:

    def test_index(self):
        client = Client()
        response = client.get('/lettings/')
        assertTemplateUsed(response, 'lettings_index.html')    

    def test_letting(self, client):
        #monkeypatch.setitem(Letting[0], 'title', title_test)
        response = client.get(reverse('lettings:letting', kwargs={"letting_id":1}))
        #response = client.get('/lettings/1/')
        #response = self.client.get(reverse('lettings:letting', args=(1,)), follow=True)
        print('///////', response.content)
        print('///////', response)
        #print('///////', reponse.redirect_chain)
        assertTemplateUsed(response, 'lettings.html')
        #path('lettings/<int:letting_id>/', views.letting, name='letting'),





@pytest.mark.django_db
class TestUser(unittest.TestCase):

    def setUp(self):
        self.fake = Faker()
        self.address = Address(
            number = self.fake.building_number(),
            street = self.fake.street_name(),
            city = self.fake.city(),
            state = self.fake.name(),
            zip_code = self.fake.postcode(),
        )
        self.letting = Letting(
            id = 1,
            title = self.fake.name(),
            address = self.address
        )
        self.client = Client()

    def test_letting_creation(self):
        self.assertIsInstance(self.letting, Letting)

    @pytest.mark.django_db
    def test_index(self):
        c = Client()
        response = c.get('/lettings/')
        assertTemplateUsed(response, 'lettings_index.html')

    @pytest.mark.django_db
    def test_letting(self, client):
        test = Letting.objects.all()
        print(test)
        title_test = 'title_test'
        #monkeypatch.setitem(Letting[0], 'title', title_test)
        data = self.letting
        print(type(data))
        print(data.address)
        print(data.id)
        
        #response = self.client.get(reverse('lettings:letting', kwargs={"letting_id":1}))
        response = client.get('/lettings/1/', data=data)
        #response = self.client.get(reverse('lettings:letting', args=(1,)), follow=True)
        print('///////', response.content)
        print('///////', response)
        #print('///////', reponse.redirect_chain)
        assertTemplateUsed(response, 'lettings.html')
        #path('lettings/<int:letting_id>/', views.letting, name='letting'),



class Test_Letting(TestCase):

    def setUp(self):
        self.fake = Faker()
        self.address = Address.objects.create(
            number = self.fake.building_number(),
            street = self.fake.street_name(),
            city = self.fake.city(),
            state = self.fake.name(),
            zip_code = self.fake.postcode(),
        )
        self.letting = Letting.objects.create(
            id = 1,
            title = self.fake.name(),
            address = self.address
        )

    def test_index(self):
        c = Client()
        response = c.get('/lettings/')
        assertTemplateUsed(response, 'lettings_index.html')

    def test_letting(self):
        letting = Letting.objects.get(id=self.letting.id)
        self.assertEqual(self.letting.title, letting.title)

    def test_letting_2(self):
        response = self.client.get(reverse('lettings:letting', kwargs={"letting_id":1}))
        #response = self.client.get('/lettings/1/')
        response = self.client.get(reverse('/lettings/1/'))
        self.assertTemplateUsed(response, 'lettings_index.html')
"""