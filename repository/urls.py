from django.urls import path
from . import views

urlpatterns = [
    path('repositories', views.RepositoryListCreate.as_view(), name='repository-list'),
    path('repositories/<int:pk>', views.RepositoryDetail.as_view(), name='repository-detail'),
]
