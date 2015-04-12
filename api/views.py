from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.models import Source, History
from api.serializers import SourceSerializer, HistorySerializer
from api.permissions import IsOwnerOrReadOnly


class SourceList(generics.ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    serializer_class = SourceSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Source.objects.all()
        sortDate = self.request.QUERY_PARAMS.get('sort_date', None)
        limit = self.request.QUERY_PARAMS.get('limit', None)
        source_id = self.request.QUERY_PARAMS.get('source_id', None)
        author = self.request.QUERY_PARAMS.get('author', None)
        print author
        if source_id is not None:
            queryset = queryset.filter(source_id=source_id)
        if author is not None:
            queryset = queryset.filter(author__user__username=author)
        if sortDate is not None:
            queryset = queryset.order_by('-last_updated')
        if limit is not None:
            queryset = queryset[:limit]
        return queryset

class SourceDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

class HistoryList(generics.ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    serializer_class = HistorySerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = History.objects.all()
        sortDate = self.request.QUERY_PARAMS.get('sort_date', None)
        limit = self.request.QUERY_PARAMS.get('limit', None)
        source_id = self.request.QUERY_PARAMS.get('source_id', None)
        author = self.request.QUERY_PARAMS.get('author', None)
        if source_id is not None:
            queryset = queryset.filter(source_id=source_id)
        if author is not None:
            queryset = queryset.filter(author__user__username=author)
        if sortDate is not None:
            queryset = queryset.order_by('-date_created')
        if limit is not None:
            queryset = queryset[:limit]
        return queryset

class HistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = History.objects.all()
    serializer_class = HistorySerializer
