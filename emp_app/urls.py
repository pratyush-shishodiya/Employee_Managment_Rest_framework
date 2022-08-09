from asyncio.proactor_events import _ProactorDuplexPipeTransport
from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import Employeeview,Departmentemployee, Roleemployee,Updateemployeeview
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('employee/',Employeeview.as_view()),
    #path('filter/',Filteremployee.as_view()),
    path('department/',Departmentemployee.as_view()),
    path('role/',Roleemployee.as_view()),
    path('employee/<int:id>',Updateemployeeview.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    
]