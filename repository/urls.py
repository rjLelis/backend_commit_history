from django.urls import path
from . import views

urlpatterns = [
    path('repositories', views.RepositoryListCreate.as_view(),
        name='repository-list-create'),
    path('repositories/<int:pk>', views.RepositoryDetail.as_view(),
        name='repository-detail'),
    path('owner', views.OwnerListCreate.as_view(),
        name='owner-list-create'),
    path('owner/<str:username>', views.owner_detail,
        name='owner-detail'),
    path('owner/<str:username>/repositories', views.repositories_by_owner,
        name='repositories-by-owner')
]
