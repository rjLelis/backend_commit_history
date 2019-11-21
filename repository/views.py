from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import Repository, Owner
from .serializers import RepositorySerializer


class RepositoryListCreate(generics.ListCreateAPIView):
    queryset = Repository.objects.order_by('-created_at').all()
    serializer_class = RepositorySerializer

    def post(self, request):
        username = request.data.get('username')
        repo_name = request.data.get('repo_name')
        repo_description = request.data.get('repo_description', '')

        if username.strip() is None or username.strip() == '':
            return Response({
                'message': 'the username of the repository most be filled'
            },
                status=status.HTTP_400_BAD_REQUEST
            )

        owner = Owner.objects.get(name=username)

        if owner is None:
            return Response({
                'message': 'the user provided is not registered'
            },
                status=status.HTTP_400_BAD_REQUEST
            )

        if repo_name.strip() is None or repo_name.strip() == '':
            return Response({
                'message': 'the repository name is must be filled'
            },
                status=status.HTTP_400_BAD_REQUEST
            )

        repo, created = Repository.objects.get_or_create(
            name=repo_name,
            description=repo_description,
            owner=owner
        )

        serializer = self.serializer_class(repo)

        if not created:
            return Response({
                'repository': serializer.data,
                'message': 'the repository provided is already saved'
            },
                status=status.HTTP_409_CONFLICT
            )

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RepositoryDetail(generics.RetrieveAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
