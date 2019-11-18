from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Repository
from .serializers import RepositorySerializer


class RepositoryListCreate(generics.ListCreateAPIView):
    queryset = Repository.objects.order_by('created_at').all()
    serializer_class = RepositorySerializer


class RepositoryDetail(generics.RetrieveAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
