from django.urls import path
from . import views

urlpatterns = [
    path('repository/<str:repository_name>', views.get_repository, name='repository-list-by-name'),
    path('repository/', views.RepositoryList.as_view(), name='repository-list')
]