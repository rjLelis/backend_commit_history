from rest_framework import serializers
from .models import Repository, Owner


class RepositorySerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Repository
        fields = ('id', 'name', 'description', 'owner', )


class OwnerSerializer(serializers.ModelSerializer):

    repositories = serializers.HyperlinkedRelatedField(
        many=True, view_name='repository-detail', read_only=True)
    class Meta:
        model = Owner
        fields = ('username', 'email', 'repositories', )
