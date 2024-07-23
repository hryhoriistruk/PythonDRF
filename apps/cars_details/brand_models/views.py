from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

from apps.cars_details.brand_models.models import CarBrandModel, CarsModelModel
from apps.cars_details.brand_models.serializers import CarBrandSerializer, CarsModelSerializer


class CarsBrandListCreateView(ListCreateAPIView):
    serializer_class = CarBrandSerializer
    queryset = CarBrandModel.objects.prefetch_related('cars_model')
    lookup_field = 'brand_models'


class CarsBrandListUpdateRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarBrandSerializer
    queryset = CarBrandModel.objects.prefetch_related('cars')
    lookup_field = 'brand'


class CarsModelListCreateView(ListCreateAPIView):
    serializer_class = CarsModelSerializer
    queryset = CarsModelModel.objects.all()
    lookup_field = 'model'


class CarsModelListUpdateRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarsModelSerializer
    queryset = CarsModelModel.objects
    lookup_field = 'model'
