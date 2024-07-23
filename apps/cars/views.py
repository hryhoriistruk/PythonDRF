from django.db.models import Q
from django.forms import model_to_dict
from django.http import Http404

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import CarFilter
# from .filters import car_filtered_queryset
from .models import CarModel
from .serializers import CarSerializer
from core.permissions.is_super_user import IsSuperUser


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    # pagination_class = PageNumberPagination
    queryset = CarModel.objects.all()
    filterset_class = CarFilter
    permission_classes = (IsSuperUser,)

    # def get_queryset(self):
    #     return car_filtered_queryset(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
