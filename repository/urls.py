from django.urls import path
from . import views

urlpatterns = [
    path('api', views.RepositoryListCreate.as_view(), name='repository-list'),
    path('api/<int:pk>', views.RepositoryDetail.as_view(), name='repository-detail'),
]
