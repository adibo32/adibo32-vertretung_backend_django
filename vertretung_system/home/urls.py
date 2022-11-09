from django.urls import path, include
from rest_framework import routers
from .views import *

from . import views

router = routers.DefaultRouter()
router.register(r'users', UserAPI)
router.register(r'usertype', UserTypeAPI)
router.register(r'allantrags', AntragAPI)

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('antrag/', views.antrag, name='antrag'),
    path('', include(router.urls)),
    
]
