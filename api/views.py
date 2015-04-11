from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.models import Source
from api.serializers import SourceSerializer
from api.permissions import IsOwnerOrReadOnly


class SourceList(generics.ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

class SourceDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
