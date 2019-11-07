from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Repository
from .serializers import RepositorySerializer
import requests

@api_view(['GET'])
def get_repository(request, repository_name):
    
    username = 'rjLelis'
    repository_url = f'https://api.github.com/repos/{username}/{repository_name}'
    api_response = requests.get(repository_url)
    
    if api_response.status_code != 200:
        return Response({
                'status': api_response.status_code, 
                'message': api_response.json().get('message')
            })
    
    new_repo = Repository.objects.create(
                name=repository_name, 
                description=api_response.json().get('description')
            )

    repo_serialized = RepositorySerializer(new_repo)

    return Response(repo_serialized.data)

class RepositoryList(generics.ListAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer