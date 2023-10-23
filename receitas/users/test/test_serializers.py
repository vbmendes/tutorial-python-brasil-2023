import pytest
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import check_password
from .factories import UserFactory
from ..serializers import CreateUserSerializer


@pytest.mark.django_db
class TestCreateUserSerializer:
    @pytest.fixture
    def user_data(self):
        return model_to_dict(UserFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = CreateUserSerializer(data={})
        assert not serializer.is_valid()

    def test_serializer_with_valid_data(self, user_data):
        serializer = CreateUserSerializer(data=user_data)
        assert serializer.is_valid()

    def test_serializer_hashes_password(self, user_data):
        serializer = CreateUserSerializer(data=user_data)
        assert serializer.is_valid()

        user = serializer.save()
        assert check_password(user_data.get("password"), user.password)
