from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import Repository
from .serializers import RepositorySerializer


class RepositoryListCreate(generics.ListCreateAPIView):
    queryset = Repository.objects.order_by('created_at').all()
    serializer_class = RepositorySerializer

    def post(self, request):
        name = request.data.get('name')
        description = request.data.get('description', '')

        if name is None or name.strip() == '':
            return Response({
                'message': 'the repository name is must be filled'
            },
                status=status.HTTP_400_BAD_REQUEST
            )

        repo, created = Repository.objects.get_or_create(
            name=name,
            description=description
        )

        if not created:
            return Response({
                'message': 'the repository is already on the list'
            },
                status=status.HTTP_400_BAD_REQUEST
            )

        repo.save()
        serializer = self.serializer_class(repo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RepositoryDetail(generics.RetrieveAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
