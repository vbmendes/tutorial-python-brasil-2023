import pytest
from rest_framework import status
from waffle.testutils import override_switch

from receitas.constants import MY_AWESOME_SWITCH


@pytest.mark.django_db
@pytest.mark.parametrize("switch_value", (True, False))
def test_switches(api_client, switch_value):
    with override_switch(MY_AWESOME_SWITCH, switch_value):
        response = api_client.get("/switches/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()[MY_AWESOME_SWITCH] == switch_value
