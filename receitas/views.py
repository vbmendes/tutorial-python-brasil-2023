from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def version(request):
    return Response({"version": settings.VERSION})
