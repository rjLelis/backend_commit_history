from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Repository


class RepositorySerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Repository
        fields = ('id', 'name', 'description', 'owner', )


class UserSerializer(serializers.ModelSerializer):

    repositories = serializers.HyperlinkedRelatedField(
        many=True, view_name='repository-detail', read_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'repositories', )
