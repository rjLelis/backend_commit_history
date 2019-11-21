from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view


@api_view(['GET'])
def home(request):
    return Response({
        'GET/POST repositories':
            reverse('repository-list-create'),
        'GET repository by id':
            reverse('repository-detail', kwargs={'pk': 0 }),
        'POST owner':
            reverse('owner-list-create')
    })

