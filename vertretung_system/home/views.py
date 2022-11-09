from django.http import HttpResponse
from .models import *
from rest_framework import viewsets
from .serializers import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    return HttpResponse("hier insert loggin.html")

def logout(request):
    return HttpResponse("hier insert loggout.html")

def formular(reques):
    return HttpResponse("hier insert formular.html")

class UserTypeAPI(viewsets.ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer


class UserAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AntragAPI(viewsets.ModelViewSet):
    queryset = Antrag.objects.all()
    serializer_class = AntragSerializer