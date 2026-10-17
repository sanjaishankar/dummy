from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .serializers import PersonSerializer


@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
def create_person(request):
    serializer = PersonSerializer(data=request.data)

    if serializer.is_valid():
        person = serializer.save()

        return Response(
            PersonSerializer(person).data,
            status=status.HTTP_201_CREATED,
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )