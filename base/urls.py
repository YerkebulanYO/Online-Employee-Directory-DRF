from django.urls import path, include
from . import views
from .views import EmployeeList
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'employees', EmployeeList)

urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
]
