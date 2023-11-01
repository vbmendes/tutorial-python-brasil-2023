from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from waffle import switch_is_active

from receitas.constants import MY_AWESOME_SWITCH


@api_view()
def version(request):
    return Response({"version": settings.VERSION})


@api_view()
def switches(request):
    return Response({MY_AWESOME_SWITCH: switch_is_active(MY_AWESOME_SWITCH)})
