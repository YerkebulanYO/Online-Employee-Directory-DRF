from django.shortcuts import render, redirect
from .models import Employee

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import EmployeeSerializer
import json
from django.http import HttpResponse
from rest_framework import mixins


class EmployeeList(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id', 'full_name', 'employment_date', 'boss', 'salary', 'position']
    ordering_fields = ('id', 'full_name', 'employment_date', 'boss', 'salary', 'position')
    permission_classes = (IsAuthenticated, )