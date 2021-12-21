import pytest
from pytest_django.asserts import assertTemplateUsed


def test_index(client):
    response = client.get('')
    assertTemplateUsed(response, 'index.html')