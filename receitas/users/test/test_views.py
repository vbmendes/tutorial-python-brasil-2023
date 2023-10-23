import pytest
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
import factory
from ..models import User
from .factories import UserFactory

fake = Faker()


@pytest.mark.django_db
class TestUserListTestCase:
    """
    Tests /users list operations.
    """

    @pytest.fixture
    def url(self):
        return reverse("user-list")

    @pytest.fixture
    def user_data(self):
        return factory.build(dict, FACTORY_CLASS=UserFactory)

    def test_post_request_with_no_data_fails(self, api_client, url):
        response = api_client.post(url, {})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_post_request_with_valid_data_succeeds(self, api_client, url, user_data):
        response = api_client.post(url, user_data)
        assert response.status_code == status.HTTP_201_CREATED

        user = User.objects.get(pk=response.data.get("id"))
        assert user.username == user_data.get("username")
        assert check_password(user_data.get("password"), user.password)


@pytest.mark.django_db
class TestUserDetailTestCase:
    """
    Tests /users detail operations.
    """

    @pytest.fixture
    def user(self):
        return UserFactory()

    @pytest.fixture
    def url(self, user):
        return reverse("user-detail", kwargs={"pk": user.pk})

    def test_get_request_returns_a_given_user(self, api_client, url):
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_put_request_updates_a_user(self, api_client, url, user):
        new_first_name = fake.first_name()
        payload = {"first_name": new_first_name}
        response = api_client.put(url, payload)
        assert response.status_code == status.HTTP_200_OK

        user = User.objects.get(pk=user.id)
        assert user.first_name == new_first_name
