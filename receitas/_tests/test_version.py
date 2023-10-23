from django.conf import settings
from rest_framework import status


def test_version(api_client):
    response = api_client.get("/version/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"version": settings.VERSION}
