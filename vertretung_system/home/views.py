from django.http import HttpResponse
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    return HttpResponse("hier insert loggin.html")

def logout(request):
    return HttpResponse("hier insert loggout.html")

@api_view(['GET', 'POST', 'DELETE'])
def antrag(request):
    if request.method == 'GET':
        antrags = Antrag.objects.all()
        
        creator_user = request.query_params.get('creator_user', None)
        if creator_user is not None:
            antrags = antrags
        
        antrags_serializer = AntragSerializer(antrags, many=True)
        return JsonResponse(antrags_serializer.data, safe=False)
    
    elif request.method == 'POST':
        antrag_data = JSONParser().parse(request)
        antrags_serializer = AntragSerializer(data=antrag_data)
        if antrags_serializer.is_valid():
            antrags_serializer.save()
            return JsonResponse(antrags_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(antrags_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

class UserTypeAPI(viewsets.ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer


class UserAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AntragAPI(viewsets.ModelViewSet):
    queryset = Antrag.objects.all()
    serializer_class = AntragSerializer