from django.contrib.auth.models import  Group
from .models import *
from rest_framework import serializers

class DominioNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dominio
        fields = ('Direction')
class InduserSerializer(serializers.ModelSerializer):
    associates =serializers.SlugRelatedField(
    slug_field='Direction',
    read_only=True,
    many=True,)
    owner = serializers.SlugRelatedField(
    slug_field='Direction',
    read_only=True,
    many=True,)
    class Meta:
        model = User
        fields = ('id','username', 'email', 'groups','Pais','Telefono','owner','associates')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email','Pais','Telefono','password')
        extra_kwargs = {
          'password': {'write_only': True}
        }
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
class DominioSerializer(serializers.ModelSerializer):
    Owner=serializers.SlugRelatedField(
    read_only=True,
    slug_field='username',
   
    )
    Associates=serializers.SlugRelatedField(
    queryset= User.objects.all(),
    slug_field='username',
    many=True,
    )
    class Meta:
        model = Dominio
        fields = ('id','Owner','Associates','Direction','Expirationdate')
class UsernameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
class DominioReadSerializer(serializers.ModelSerializer):
    Owner=serializers.SlugRelatedField(
    read_only=True,
    slug_field='username',
   
    )
    Associates= UserSerializer(many=True,read_only=True)
    class Meta:
        model = Dominio
        fields = ('id','Owner','Associates','Direction','Expirationdate','Expired')
class DateSerializer(serializers.Serializer):
    today = serializers.DateTimeField()
