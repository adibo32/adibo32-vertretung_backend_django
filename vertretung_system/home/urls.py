from django.urls import path, include
from rest_framework import routers
from .views import *

from . import views

router = routers.DefaultRouter()
router.register(r'users', UserAPI)
router.register(r'usertype', UserTypeAPI)
router.register(r'antrag', AntragAPI)

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', include(router.urls)),
    
]
