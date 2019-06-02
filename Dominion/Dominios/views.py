from django.shortcuts import render
from Dominios.models import *
from Dominios.serializers import *
from rest_framework import generics,permissions
from Dominios.permissions import IsOwnerOrReadOnly
from datetime import date
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = InduserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'username'
class DominiosList(generics.ListCreateAPIView):
    queryset = Dominio.objects.all()
    serializer_class = DominioSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
     serializer.save(Owner=self.request.user)
class DominiosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dominio.objects.all()
    serializer_class = DominioSerializer 
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    lookup_field = 'Direction'
class Usernamelist(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsernameSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
class DominioReadlist(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dominio.objects.all()
    serializer_class = DominioReadSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'Direction'
class DominioExpiredlist(generics.ListCreateAPIView):
    queryset = Dominio.objects.all().filter(Expired=True)
    serializer_class = DominioReadSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
@api_view(['GET'])    
def GetTime(request):
    strdate = str(date.today())
    strdata = {"today": strdate}
    serializer = DateSerializer(strdata)
    return Response(serializer.data)